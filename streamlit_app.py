import io
import pandas as pd
import streamlit as st
import plotly.express as px
from ml_models.demand_forecasting import DemandForecaster


def load_input_data(data_source: str, uploaded_file=None, sample_days: int = 60):
    if data_source == "Upload CSV":
        if uploaded_file is None:
            return None

        try:
            df = pd.read_csv(uploaded_file, parse_dates=["date"])
        except Exception:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file)
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"], errors="coerce")

        return df

    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=sample_days)
    quantities = (pd.Series(range(sample_days)) * 0.1 + 50).astype(int)
    return pd.DataFrame({"date": dates, "quantity_sold": quantities})


def prepare_dataframe(df):
    if df is None:
        return None

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame.")

    required_columns = {"date", "quantity_sold"}
    if not required_columns.issubset(df.columns):
        raise ValueError("Input data must include 'date' and 'quantity_sold' columns.")

    cleaned_df = df.copy()
    if not pd.api.types.is_datetime64_any_dtype(cleaned_df["date"]):
        cleaned_df["date"] = pd.to_datetime(cleaned_df["date"], errors="coerce")

    cleaned_df = cleaned_df.dropna(subset=["date", "quantity_sold"])
    if cleaned_df.empty:
        return cleaned_df

    return cleaned_df.sort_values("date").reset_index(drop=True)


def main():
    st.set_page_config(page_title="Demand Forecasting", layout="wide")
    st.title("Food / Restaurant Demand Forecasting — Streamlit UI")

    st.sidebar.header("Data & Model")

    data_source = st.sidebar.radio("Data source", ("Upload CSV", "Use sample data"))
    uploaded = None
    sample_days = 60

    if data_source == "Upload CSV":
        uploaded = st.sidebar.file_uploader("Upload CSV with columns: date, quantity_sold", type=["csv"])
    else:
        sample_days = st.sidebar.number_input("Sample days", min_value=30, max_value=365, value=60)

    st.sidebar.markdown("---")
    model_type = st.sidebar.selectbox("Model type", ("random_forest",))
    days_to_forecast = st.sidebar.slider("Days to forecast", min_value=1, max_value=90, value=14)
    random_state = st.sidebar.number_input("Random seed", min_value=0, max_value=9999, value=42)
    train_button = st.sidebar.button("Train & Forecast")

    # show data preview
    st.subheader("Input data")
    df = load_input_data(data_source, uploaded_file=uploaded, sample_days=int(sample_days))

    try:
        df = prepare_dataframe(df)
    except (TypeError, ValueError) as exc:
        st.error(str(exc))
        st.stop()

    if df is None:
        st.warning("No data provided yet.")
        st.stop()

    if df.empty:
        st.error("The uploaded data contains no valid rows after cleaning. Please provide a file with valid date and quantity_sold values.")
        st.stop()

    st.dataframe(df.tail(50))

    # validate minimum rows
    if len(df) < 30:
        st.error("At least 30 records required for training. Provide more data or increase sample days.")
        st.stop()

    # model object
    forecast_model = DemandForecaster(model_type=model_type, random_state=int(random_state))

    if train_button:
        with st.spinner("Training model..."):
            try:
                metrics = forecast_model.train(df)
            except Exception as exc:
                st.error(f"Training failed: {exc}")
                st.stop()

        st.success("Model trained")
        st.subheader("Training metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("MAE", f"{metrics.get('mae', float('nan')):.4f}")
        col2.metric("RMSE", f"{metrics.get('rmse', float('nan')):.4f}")
        col3.metric("R²", f"{metrics.get('r2', float('nan')):.4f}")

        with st.spinner("Generating forecast..."):
            try:
                forecast_rows = forecast_model.forecast(df, days_ahead=int(days_to_forecast))
            except Exception as exc:
                st.error(f"Forecast failed: {exc}")
                st.stop()

        forecast_df = pd.DataFrame(forecast_rows)
        forecast_df["date"] = pd.to_datetime(forecast_df["date"])
        st.subheader(f"{days_to_forecast}-day forecast")
        st.dataframe(forecast_df)

        # chart: historical + forecast
        hist = df[["date", "quantity_sold"]].rename(columns={"quantity_sold": "value"})
        hist["type"] = "historical"
        fc = forecast_df.rename(columns={"predicted_quantity": "value"})
        fc["type"] = "forecast"
        combined = pd.concat([hist, fc], ignore_index=True)
        fig = px.line(combined, x="date", y="value", color="type", labels={"value": "Quantity"})
        st.plotly_chart(fig, use_container_width=True)

        # prepare CSV download
        csv_buf = io.StringIO()
        forecast_df.to_csv(csv_buf, index=False)
        st.download_button("Download forecast CSV", csv_buf.getvalue(), file_name="forecast.csv", mime="text/csv")

    else:
        st.info("Configure options in the sidebar and click 'Train & Forecast' to run the model.")


if __name__ == "__main__":
    main()
