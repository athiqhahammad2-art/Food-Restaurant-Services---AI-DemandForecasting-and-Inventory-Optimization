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

**Version:** 1.1.0
**Last Updated:** 2026-07-02
