import numpy as np
import pandas as pd
from datetime import timedelta

try:
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
except ImportError as exc:
    raise ImportError(
        "scikit-learn is required to use DemandForecaster. Install it with `pip install scikit-learn`."
    ) from exc


class DemandForecaster:
    def __init__(self, model_type='random_forest', random_state=42):
        self.model_type = model_type
        self.random_state = random_state
        self.model = None
        self.is_trained = False
        self.feature_columns = None

    def _validate_data(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Training data must be a pandas DataFrame.')

        required_columns = {'date', 'quantity_sold'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f'Training data must include columns: {required_columns}')

        if len(data) < 30:
            raise ValueError('Insufficient data: at least 30 records are required for training.')

        if not np.issubdtype(data['date'].dtype, np.datetime64):
            data = data.copy()
            data['date'] = pd.to_datetime(data['date'])

        data = data.sort_values('date').reset_index(drop=True)
        return data

    def _create_features(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df['day_of_week'] = df['date'].dt.weekday
        df['month'] = df['date'].dt.month
        df['week_of_year'] = df['date'].dt.isocalendar().week.astype(int)
        df['lag_1'] = df['quantity_sold'].shift(1)
        df['lag_7'] = df['quantity_sold'].shift(7)
        df['rolling_7'] = df['quantity_sold'].rolling(window=7, min_periods=1).mean()
        df['rolling_14'] = df['quantity_sold'].rolling(window=14, min_periods=1).mean()
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        df = df.dropna().reset_index(drop=True)
        return df

    def train(self, data: pd.DataFrame) -> dict:
        data = self._validate_data(data)
        features = self._create_features(data)

        feature_columns = [
            'day_of_week',
            'month',
            'week_of_year',
            'lag_1',
            'lag_7',
            'rolling_7',
            'rolling_14',
            'is_weekend'
        ]
        target_column = 'quantity_sold'

        X = features[feature_columns]
        y = features[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=self.random_state
        )

        if self.model_type == 'random_forest':
            self.model = RandomForestRegressor(
                n_estimators=100,
                random_state=self.random_state,
                n_jobs=-1
            )
        else:
            raise ValueError(f'Unsupported model_type: {self.model_type}')

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        metrics = {
            'mae': float(mean_absolute_error(y_test, y_pred)),
            'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred))),
            'r2': float(r2_score(y_test, y_pred))
        }

        self.feature_columns = feature_columns
        self.is_trained = True
        self.last_training_data = data.copy()
        return metrics

    def forecast(self, historical_data: pd.DataFrame, days_ahead: int = 30) -> list:
        if not self.is_trained or self.model is None:
            raise ValueError('The model must be trained before forecasting.')

        if days_ahead <= 0:
            raise ValueError('days_ahead must be greater than zero.')

        historical = self._validate_data(historical_data)
        historical = historical.sort_values('date').reset_index(drop=True)

        forecast_data = historical.tail(14).copy()
        forecast_data = forecast_data.reset_index(drop=True)
        forecast_rows = []

        for step in range(days_ahead):
            last_date = forecast_data.loc[forecast_data.index[-1], 'date']
            next_date = last_date + timedelta(days=1)
            next_row = {
                'date': next_date,
                'day_of_week': next_date.weekday(),
                'month': next_date.month,
                'week_of_year': int(next_date.isocalendar()[1]),
                'is_weekend': int(next_date.weekday() in [5, 6])
            }

            last_quantity = forecast_data.loc[forecast_data.index[-1], 'quantity_sold']
            seven_day_ago_index = len(forecast_data) - 7
            next_row['lag_1'] = last_quantity
            next_row['lag_7'] = (
                forecast_data.loc[seven_day_ago_index, 'quantity_sold']
                if seven_day_ago_index >= 0 else last_quantity
            )
            next_row['rolling_7'] = float(forecast_data['quantity_sold'].tail(7).mean())
            next_row['rolling_14'] = float(forecast_data['quantity_sold'].tail(14).mean())

            feature_vector = pd.DataFrame([next_row])[self.feature_columns]
            predicted_quantity = max(0.0, float(self.model.predict(feature_vector)[0]))

            forecast_rows.append({
                'date': next_date.date(),
                'predicted_quantity': predicted_quantity
            })

            next_row['quantity_sold'] = predicted_quantity
            forecast_data = pd.concat([forecast_data, pd.DataFrame([next_row])], ignore_index=True)

        return forecast_rows
