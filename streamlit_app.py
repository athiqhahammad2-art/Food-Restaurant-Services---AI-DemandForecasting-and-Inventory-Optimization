import io
import pandas as pd
import streamlit as st
import plotly.express as px
from ml_models.demand_forecasting import DemandForecaster

st.set_page_config(page_title="Demand Forecasting", layout="wide")

st.title("Food / Restaurant Demand Forecasting — Streamlit UI")

st.sidebar.header("Data & Model")

data_source = st.sidebar.radio("Data source", ("Upload CSV", "Use sample data"))

if data_source == "Upload CSV":
    uploaded = st.sidebar.file_uploader("Upload CSV with columns: date, quantity_sold", type=["csv"])
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded, parse_dates=["date"])
        except Exception:
            uploaded.seek(0)
            df = pd.read_csv(uploaded)
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
else:
    # generate a sample dataset (60 days) similar to run_forecast.py
    days = st.sidebar.number_input("Sample days", min_value=30, max_value=365, value=60)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days)
    quantities = (pd.Series(range(days)) * 0.1 + 50).astype(int)
    df = pd.DataFrame({"date": dates, "quantity_sold": quantities})

st.sidebar.markdown("---")
model_type = st.sidebar.selectbox("Model type", ("random_forest",))
days_to_forecast = st.sidebar.slider("Days to forecast", min_value=1, max_value=90, value=14)
random_state = st.sidebar.number_input("Random seed", min_value=0, max_value=9999, value=42)
train_button = st.sidebar.button("Train & Forecast")

# show data preview
st.subheader("Input data")
if df is None or df.empty:
    st.warning("No data provided yet.")
    st.stop()

# ensure date column is datetime and sorted
df = df.copy()
if not pd.api.types.is_datetime64_any_dtype(df["date"]):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "quantity_sold"]) 
df = df.sort_values("date").reset_index(drop=True)

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
        except Exception as e:
            st.error(f"Training failed: {e}")
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
        except Exception as e:
            st.error(f"Forecast failed: {e}")
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
