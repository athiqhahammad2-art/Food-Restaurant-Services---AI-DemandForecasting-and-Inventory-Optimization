import unittest
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from ml_models.demand_forecasting import DemandForecaster

class TestDemandForecasting(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.forecaster = DemandForecaster(model_type='random_forest')
        self.sample_data = self._generate_sample_data()
    
    def _generate_sample_data(self, days=100):
        """Generate sample historical data"""
        dates = [datetime.utcnow().date() - timedelta(days=x) for x in range(days, 0, -1)]
        quantities = np.random.poisson(lam=50, size=days) + np.sin(np.arange(days) * 2 * np.pi / 7) * 10
        
        df = pd.DataFrame({
            'date': dates,
            'quantity_sold': quantities.astype(int),
            'day_of_week': [d.weekday() for d in dates],
            'is_holiday': [False] * days
        })
        
        return df
    
    def test_model_training(self):
        """Test model training with sufficient data"""
        metrics = self.forecaster.train(self.sample_data)
        
        self.assertIn('mae', metrics)
        self.assertIn('rmse', metrics)
        self.assertIn('r2', metrics)
        self.assertGreaterEqual(metrics['r2'], 0)
        self.assertLessEqual(metrics['r2'], 1)
        self.assertTrue(self.forecaster.is_trained)
    
    def test_insufficient_training_data(self):
        """Test error handling with insufficient data"""
        small_data = self.sample_data.head(20)
        
        with self.assertRaises(ValueError):
            self.forecaster.train(small_data)
    
    def test_forecast_generation(self):
        """Test demand forecast generation"""
        self.forecaster.train(self.sample_data)
        forecasts = self.forecaster.forecast(self.sample_data, days_ahead=30)
        
        self.assertEqual(len(forecasts), 30)
        
        for forecast in forecasts:
            self.assertIn('date', forecast)
            self.assertIn('predicted_quantity', forecast)
            self.assertGreaterEqual(forecast['predicted_quantity'], 0)

if __name__ == '__main__':
    unittest.main()