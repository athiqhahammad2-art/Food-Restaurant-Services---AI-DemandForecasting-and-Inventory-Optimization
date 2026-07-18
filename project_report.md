# Project Report: Food Restaurant Services — AI Demand Forecasting & Inventory Optimization

## 1. Executive Summary

This project is a restaurant-focused AI solution designed to forecast demand and support inventory optimization decisions. The system combines a machine learning pipeline, a Streamlit web app, and a frontend dashboard to provide restaurant managers with insights into expected sales, stock requirements, and operational planning.

The repository currently focuses on the core forecasting component and presentation layer. It demonstrates how historical sales data can be converted into actionable predictions using a Random Forest-based regression model, along with a simple visualization interface for end users.

## 2. Project Objective

The main goals of the project are to:

- Predict future product demand using historical sales data.
- Reduce overstocking and stockouts through forecast-driven planning.
- Provide an interactive dashboard for viewing metrics and forecasts.
- Demonstrate a practical AI workflow for restaurant inventory management.

## 3. Overall Architecture

The project is organized as a lightweight end-to-end prototype with the following layers:

1. Data Layer
   - Historical sales data is provided in a pandas DataFrame with at least two key columns: date and quantity_sold.

2. Machine Learning Layer
   - A custom DemandForecaster class trains a Random Forest regressor using engineered features such as weekday, month, lag values, and rolling averages.

3. User Interface Layer
   - A Streamlit app provides a simple interactive experience for uploading or generating data, training a model, and viewing forecasts.
   - A static HTML/CSS/JavaScript dashboard presents a richer UI experience with charts and navigation.

4. Testing Layer
   - Unit tests validate training, error handling, and forecast generation.

## 4. Repository Structure

The repository contains the following major components:

- [README.md](README.md) – High-level project description, feature overview, setup instructions, and deployment notes.
- [requirements.txt](requirements.txt) – Python dependencies required to run the project.
- [run_forecast.py](run_forecast.py) – Command-line script that trains and evaluates the forecasting model.
- [streamlit_app.py](streamlit_app.py) – Interactive Streamlit interface for data upload, training, and forecasting.
- [ml_models/demand_forecasting.py](ml_models/demand_forecasting.py) – Core machine learning implementation.
- [ml_models/__init__.py](ml_models/__init__.py) – Package initializer for the machine learning module.
- [frontend/index.html](frontend/index.html) – Dashboard layout and UI sections.
- [frontend/script.js](frontend/script.js) – Client-side behavior and chart initialization.
- [frontend/styles.css](frontend/styles.css) – Styling for the dashboard.
- [frontend/README.md](frontend/README.md) – Frontend-specific documentation.
- [tests/test_demand_forecasting.py](tests/test_demand_forecasting.py) – Automated tests for the forecasting module.
- [Internship_2nd_Project.ipynb](Internship_2nd_Project.ipynb) – Notebook that likely contains exploratory work or prototype analysis.

## 5. Key Components and Their Roles

### 5.1 Machine Learning Module

The main forecasting logic is implemented in [ml_models/demand_forecasting.py](ml_models/demand_forecasting.py).

Key features include:

- Validation of input data to ensure it contains date and quantity_sold columns.
- Feature engineering using:
  - day_of_week
  - month
  - week_of_year
  - lag_1
  - lag_7
  - rolling_7
  - rolling_14
  - is_weekend
- Training using RandomForestRegressor.
- Evaluation with MAE, RMSE, and R² metrics.
- Forecast generation for future days using recursive feature construction.

This approach is practical for a prototype and demonstrates the use of time-series-inspired features in a tabular learning context.

### 5.2 Command-Line Runner

The script [run_forecast.py](run_forecast.py) provides a simple entry point for:

- Generating sample data.
- Training the model.
- Printing training metrics.
- Producing a short-term forecast.

This is useful as a lightweight demonstration or for quick testing in a terminal.

### 5.3 Streamlit Application

The file [streamlit_app.py](streamlit_app.py) adds a user-friendly web-based interface where a user can:

- Upload a CSV file with historical sales data.
- Or use automatically generated sample data.
- Configure the model type and forecast horizon.
- Train the model and view forecast results.
- Download the forecast as a CSV file.

This component makes the project more accessible to non-technical users.

### 5.4 Frontend Dashboard

The frontend is built with HTML, CSS, and JavaScript and is implemented through:

- [frontend/index.html](frontend/index.html) – Dashboard layout and structure.
- [frontend/script.js](frontend/script.js) – Interactive behavior and chart rendering.
- [frontend/styles.css](frontend/styles.css) – Responsive styling and visual design.

The dashboard includes sections for:

- Overview metrics
- Demand forecasting
- Inventory optimization
- Analytics and trends
- Supplier management
- Menu item overview

Although many values are sample/demo content, the UI is well-structured and gives a strong impression of the intended product experience.

### 5.5 Testing Suite

The tests in [tests/test_demand_forecasting.py](tests/test_demand_forecasting.py) verify:

- That the model can train successfully with adequate data.
- That training fails for insufficient records.
- That forecast generation returns the expected number of predictions with valid output values.

This provides a good foundation for future reliability improvements.

## 6. Data Flow

A typical workflow in the project is:

1. A user provides historical sales data.
2. The data is validated and sorted by date.
3. Features are engineered from the historical values.
4. A regression model is trained on the engineered data.
5. Forecasts are generated for future dates.
6. The results are displayed through the Streamlit app or frontend dashboard.

## 7. Technology Stack

The project relies on the following technologies:

- Python
- pandas
- numpy
- scikit-learn
- Streamlit
- Plotly
- HTML/CSS/JavaScript
- Chart.js
- pytest

These choices make the project lightweight, accessible, and suitable for rapid prototyping.

## 8. Strengths

- Clear and focused problem statement.
- Functional machine learning prototype with measurable evaluation metrics.
- Good separation between model logic, UI, and tests.
- Interactive Streamlit experience for experimentation.
- Attractive dashboard design and modern UI structure.
- Good documentation and deployment notes in [README.md](README.md).

## 9. Observed Gaps and Improvement Areas

While the project is promising, several opportunities for improvement are visible:

- The README describes a more complete backend system with Flask/SQLAlchemy/API modules, but the current repository snapshot mainly contains the forecasting core and UI assets.
- The dashboard currently uses mock/demo values rather than live backend data in many sections.
- The forecasting logic is a useful prototype, but it could be expanded to support more realistic time-series approaches and external factors such as promotions, holidays, or weather.
- The frontend is designed well, but it would benefit from live API integration with a backend service for true end-to-end functionality.
- The training data validation is basic and could be strengthened with richer handling of missing values, seasonal trends, and outlier detection.

## 10. Overall Assessment

This repository is a strong educational and demonstration project for AI-based demand forecasting in a restaurant context. It successfully combines machine learning, interactive visualization, and a polished user interface in a compact and understandable structure.

Its current state is best described as a functional prototype rather than a full production-grade inventory management system. However, it provides a solid foundation for extending into a real-world platform with a robust backend, database integration, and more advanced forecasting capabilities.

## 11. Suggested Next Steps

To evolve this project further, the following steps would be valuable:

1. Implement a real backend API for dashboard metrics and inventory recommendations.
2. Connect the frontend to live data instead of static sample values.
3. Add more advanced forecasting models such as Prophet, XGBoost, or LSTM.
4. Include inventory optimization logic based on sales forecasts.
5. Expand automated tests and add CI/CD workflows.
6. Deploy the app in a production-like environment for live demonstration.
