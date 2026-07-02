# Food Restaurant Services — AI Demand Forecasting & Inventory Optimization

A modular system that helps restaurants predict demand and optimize inventory using AI models, actionable analytics, and an interactive frontend dashboard.

## Quick Overview

- Purpose: Reduce waste and stockouts by forecasting demand and recommending inventory actions.
- Key components: Database (SQLAlchemy), AI forecasting models, inventory optimizer, Flask REST API, and a lightweight frontend dashboard.

## Highlights

- Demand forecasting using feature engineering (lags, rolling statistics) and Random Forest models.
- Inventory optimization with EOQ, safety stock, reorder point calculations and stockout risk assessment.
- REST API to train models, fetch forecasts, and get inventory recommendations.
- Frontend dashboard (HTML/CSS/JS) for visualization and quick actions (generate purchase orders, add suppliers/menu items).
- Docker Compose setup for local dev (Postgres + Redis + backend + frontend).

## Project Structure (high level)

- backend/
  - models/ (SQLAlchemy ORM models: MenuItem, SalesRecord, Inventory, Supplier, PurchaseOrder, ForecastModel, Forecast)
  - api/ (Flask blueprints: menu, forecasting, inventory, suppliers, analytics)
  - ml/ (demand forecaster, optimizer, training scripts)
  - tests/ (unit tests for forecasting & optimization)
- frontend/
  - index.html
  - styles.css
  - script.js

## Features

- Menu Management: CRUD for menu items and sales recording
- Demand Forecasting: Train models, predict future demand with confidence intervals, view model metrics (MAE, RMSE, R²)
- Inventory Optimization: EOQ, safety stock, reorder points, and purchase order suggestions
- Supplier Management: Maintain suppliers and create purchase orders
- Analytics: Sales trends, top items, inventory turnover, waste analysis

## Technology Stack

- Backend: Python, Flask, SQLAlchemy, scikit-learn
- Database: PostgreSQL
- Cache: Redis
- Frontend: HTML, CSS, JavaScript (Chart.js, Axios)
- Dev: Docker, Docker Compose

## Getting Started (development)

1. Clone the repo

   git clone https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization.git
   cd Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization

2. Configure environment

   - Copy `.env.example` to `.env` and update DB/Redis credentials.

3. Start with Docker Compose (recommended)

   docker-compose up --build

4. Run tests

   cd backend
   pytest -q

5. Open frontend

   - Open `frontend/index.html` in your browser, or serve it with a local server: `python -m http.server 8000` and visit `http://localhost:8000`.

## API Endpoints (examples)

- GET /api/analytics/dashboard — Dashboard metrics
- GET /api/forecasting/predict — Demand predictions
- GET /api/inventory/optimization — Inventory recommendations
- GET /api/analytics/sales-trends — Sales history
- POST /api/purchase-orders/generate — Generate purchase orders


## Recent commits (latest 5)

- Add frontend README documentation — Attar Athiqh Ahammad — 2026-07-01T17:07:18Z
  https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization/commit/194d75259a9683cb40f1be7586bec8a6c61fce30

- Add comprehensive UI dashboard for project output visualization — Attar Athiqh Ahammad — 2026-07-01T17:04:18Z
  https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization/commit/9bb27a35b264985f9ca5ada23a1231e3ae70df43

- Add comprehensive styling for the dashboard UI — Attar Athiqh Ahammad — 2026-07-01T17:04:06Z
  https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization/commit/c1c68525c8d023a6c58be91ac460b50d0cbc7667

- Add JavaScript functionality for dashboard interactivity — Attar Athiqh Ahammad — 2026-07-01T17:00:09Z
  https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization/commit/b6c32377ccbc92c2b08371dce85557c5a0ceb0f8

- Add demand forecasting model, requirements, and demo runner — Attar Athiqh Ahammad — 2026-07-01T13:11:28Z
  https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization/commit/18314425c06a5190bef4d5b49c2463024d430bbd

View more commits: https://github.com/athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization/commits?per_page=5

## Contributing

1. Fork the repo
2. Create a feature branch
3. Implement and test changes
4. Open a pull request with a clear description

## License

This project is provided as-is for demonstration of AI demand forecasting and inventory optimization concepts. Add a license file if you intend to open-source it.

---

## Streamlit Deployment (Community Cloud)

You can deploy the Streamlit app (streamlit_app.py) to Streamlit Community Cloud (share.streamlit.io) for a quick public demo.

Steps to deploy

1. Open https://share.streamlit.io and sign in with your GitHub account.
2. Click "New app" → choose your repository: `athiqhahammad2-art/Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization`.
3. Set Branch: `main` and Main file: `streamlit_app.py`.
4. Click "Deploy". Streamlit Cloud will install packages from `requirements.txt` automatically and start the app.
5. After deployment, open the public app URL shown by Streamlit.

Important notes

- Ensure `streamlit_app.py` is at the repository root (it is) so the import `from ml_models.demand_forecasting import DemandForecaster` works correctly.
- requirements.txt must include `streamlit` and `plotly` (already added). If you add new dependencies, update requirements.txt and redeploy or trigger a rebuild.
- Streamlit Community Cloud builds on-demand; check the build logs for package install errors.

Troubleshooting & Logs

- Where to find logs:
  - In the deployed app page on Streamlit Cloud, open the "Logs" panel to see both build (pip install) and runtime logs (stderr/stdout).
  - Locally, run `streamlit run streamlit_app.py` and watch the terminal output for errors and stack traces.

- Common issues and fixes:

  - ImportError: No module named 'ml_models'
    - Cause: Streamlit might not be running from the repository root or the package path is not set.
    - Quick fix: ensure `streamlit_app.py` is at repo root and redeploy. Locally, run from project root: `streamlit run streamlit_app.py`.
    - Temporary workaround (not required if structure is correct): add at top of `streamlit_app.py`:

      ```python
      import os, sys
      sys.path.append(os.path.dirname(__file__))
      ```

  - pip install errors during build
    - Cause: missing system dependencies or conflicting package versions.
    - Fix: Check the build log for the failing package; pin compatible versions in requirements.txt or add necessary system-level libs to the build image if required.

  - App crashes or OOM during training
    - Cause: Training large models or large datasets on Streamlit Cloud can hit memory/time limits.
    - Fix: Reduce sample size, lower `n_estimators`, decrease `days_to_forecast`, or train offline and upload a serialized model instead.

  - Runtime errors (ValueError / TypeError)
    - Cause: Unexpected CSV formats or missing columns.
    - Fix: Ensure uploaded CSV has columns `date` and `quantity_sold`, or use the app's sample dataset. Consider adding a column-mapping UI if you need flexibility.

- If you encounter an issue you can't resolve, collect the following and open an issue in this repo:
  1. Deployment build logs (copy from Streamlit Cloud Logs).
  2. Runtime stack trace (from Logs panel or terminal).
  3. A minimal sample CSV that reproduces the error (if related to data).

---

**Version:** 1.1.0
**Last Updated:** 2026-07-02
