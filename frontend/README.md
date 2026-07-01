# Frontend UI Dashboard

A comprehensive, modern web dashboard for visualizing AI-powered demand forecasting and inventory optimization results for the restaurant management system.

## Overview

This frontend provides a beautiful, interactive interface to display:
- **Real-time Dashboard**: KPI cards showing total sales, inventory levels, low stock items, and forecast accuracy
- **Demand Forecasting**: AI predictions with confidence intervals, model metrics, and feature importance analysis
- **Inventory Optimization**: EOQ analysis, safety stock distribution, and optimization recommendations
- **Analytics & Trends**: Sales trends, top items, inventory turnover, and waste analysis
- **Supplier Management**: Supplier tracking and purchase order management
- **Menu Items**: Menu item display and management

## Features

### 📊 Dashboard Section
- Real-time KPI metrics
- Sales vs Forecast comparison chart
- Inventory level distribution
- Critical stock alerts
- Recommended purchase orders

### 📈 Demand Forecasting
- 10-day demand forecast with confidence intervals
- Model performance metrics (MAE, RMSE, R² Score)
- Feature importance analysis
- Historical and predicted demand comparison

### 📦 Inventory Optimization
- Economic Order Quantity (EOQ) calculations
- Safety stock distribution visualization
- Stockout risk assessment
- Cost optimization recommendations
- Purchase order generation

### 📉 Analytics & Trends
- 30-day sales trends
- Top performing menu items
- Inventory turnover ratio tracking
- Waste and spoilage analysis
- System health report

### 🚚 Supplier Management
- Supplier database and ratings
- Contact information and delivery times
- Easy supplier addition

### 🍽️ Menu Items
- Menu item display with pricing
- Sales and profit metrics
- Quick edit functionality

## Technology Stack

- **Frontend Framework**: HTML5, CSS3, JavaScript (Vanilla)
- **Charting Library**: Chart.js
- **HTTP Client**: Axios
- **Styling**: Custom CSS with CSS variables for theming
- **Responsive**: Mobile-first responsive design

## File Structure

```
frontend/
├── index.html          # Main dashboard HTML
├── styles.css          # Comprehensive styling
├── script.js           # JavaScript functionality
└── README.md           # This file
```

## Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Backend API running on `http://localhost:5000`

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd frontend
```

2. **Open in browser**
```bash
# Simply open index.html in your browser
open index.html

# Or use a local server
python -m http.server 8000
# Visit http://localhost:8000
```

3. **Configure API Base URL**
Edit `script.js` and update the API_BASE_URL if your backend runs on a different port:
```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## API Integration

The dashboard integrates with the backend REST API. Key endpoints used:

- `GET /api/analytics/dashboard` - Dashboard metrics
- `GET /api/forecasting/predict` - Demand predictions
- `GET /api/inventory/optimization` - Inventory recommendations
- `GET /api/analytics/sales-trends` - Sales data
- `POST /api/purchase-orders/generate` - Generate orders

## Usage Guide

### Navigation
Click on menu items in the sidebar to navigate between sections:
- 📊 **Dashboard** - Overview of key metrics
- 📈 **Demand Forecast** - AI-powered demand predictions
- 📦 **Inventory Optimization** - Stock optimization recommendations
- 📉 **Analytics & Trends** - Historical analysis and insights
- 🚚 **Suppliers** - Supplier management
- 🍽️ **Menu Items** - Menu management

### Key Actions

**Refresh Data**
Click the 🔄 Refresh button to reload all dashboard data

**Generate Purchase Orders**
Navigate to Inventory Optimization and click "Generate Purchase Orders" to auto-generate optimal orders

**Order Items**
Click the "Order" button next to critical stock items to place orders

**Add Supplier**
Click "Add Supplier" to add a new supplier to the database

**Add Menu Item**
Click "Add Menu Item" to add new menu items

### Date Filtering
Use the date picker in the header to filter data by date

## Customization

### Theme Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f5576c;
    --success-color: #43e97b;
    --warning-color: #ffa502;
    --danger-color: #ff6b6b;
}
```

### Responsive Breakpoints
Modify media queries in `styles.css` for different screen sizes:
- 1200px and below: Single column charts
- 768px and below: Mobile-optimized layout

### Chart Configuration
Customize charts in `script.js` functions:
- `initOverviewCharts()` - Dashboard charts
- `initDemandCharts()` - Forecasting charts
- `initInventoryCharts()` - Optimization charts
- `initAnalyticsCharts()` - Analytics charts

## Performance Optimization

- Charts are rendered only when sections are opened (lazy loading)
- Responsive images and CSS variables for efficient styling
- Minimal JavaScript dependencies (Chart.js + Axios)
- Optimized for both desktop and mobile devices

## Browser Support

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Troubleshooting

### Charts Not Displaying
1. Check browser console for errors (F12)
2. Verify Chart.js library is loaded
3. Ensure backend API is running and accessible

### API Connection Errors
1. Verify backend server is running on port 5000
2. Check CORS settings on backend
3. Verify API_BASE_URL in script.js matches your backend

### Styling Issues
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh page (Ctrl+F5)
3. Check for CSS conflicts in browser inspector

## Contributing

1. Create a feature branch
2. Make your changes
3. Test on multiple browsers
4. Submit a pull request

## License

This project is part of the Food Restaurant AI Demand Forecasting and Inventory Optimization system.

## Support

For issues or questions, please open an issue in the repository.

---

**Version**: 1.0.0  
**Last Updated**: July 2026
