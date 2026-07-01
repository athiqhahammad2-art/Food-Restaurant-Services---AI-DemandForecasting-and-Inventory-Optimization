import pandas as pd
from ml_models.demand_forecasting import DemandForecaster


def generate_sample_data(days=60):
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days)
    quantities = (pd.Series(range(days)) * 0.1 + 50).astype(int)
    return pd.DataFrame({
        'date': dates,
        'quantity_sold': quantities,
    })


def main():
    data = generate_sample_data(days=60)
    model = DemandForecaster(model_type='random_forest')

    print('Training model...')
    metrics = model.train(data)
    print('Training metrics:')
    for name, value in metrics.items():
        print(f'  {name}: {value:.4f}')

    print('\nGenerating 14-day forecast...')
    forecast = model.forecast(data, days_ahead=14)
    for row in forecast:
        print(f"{row['date']}: {row['predicted_quantity']:.2f}")


if __name__ == '__main__':
    main()
