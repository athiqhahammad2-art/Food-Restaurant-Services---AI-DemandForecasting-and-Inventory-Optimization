# Food-Restaurant-Services---AI-DemandForecasting-and-Inventory-Optimization
📦 Project Structure Created:
Database Layer
SQLAlchemy ORM models with 8 main tables:
MenuItem - Menu items management
SalesRecord - Historical sales data
Inventory - Stock level tracking
Supplier - Supplier information
PurchaseOrder - Purchase orders
ForecastModel - ML model metadata
Forecast - Demand predictions
AI/ML Models
DemandForecaster - Random Forest-based demand prediction with:

Lag features and rolling averages
Confidence intervals
Feature importance analysis
Model performance metrics (MAE, RMSE, R²)
InventoryOptimizer - Advanced inventory management with:

Economic Order Quantity (EOQ) calculation
Safety stock determination
Reorder point optimization
Stockout risk assessment
Actionable recommendations
REST API Endpoints (Flask Blueprints)
Menu Management: CRUD operations, sales recording
Demand Forecasting: Model training, predictions, accuracy tracking
Inventory Optimization: Stock level analysis, order suggestions
Supplier Management: Supplier tracking, purchase orders
Analytics: Sales summaries, trends, health reports
Infrastructure
Docker & Docker Compose setup
PostgreSQL database
Redis caching layer
Environment configuration
Comprehensive API documentation
Testing
Unit tests for demand forecasting
Unit tests for inventory optimization
