# Model Comparison

## Performance Metrics

### Random Forest Regression
- R² Score: 0.870119
- MSE: 22092850.821999095
- MAE: 2517.226896105666
- RMSE: 4700.303269518

### LightGBM Regression
- R² Score: 0.857690
- MSE: 24206940.918975655
- MAE: 2810.779983849323
- RMSE: 4920.054971133519

### XGBoost Regression
- R² Score: 0.838107
- MSE: 27538033.0559948
- MAE: 2890.014836327836
- RMSE: 5247.669297506733

### Linear Regression
- R² Score: 0.773276
- MSE: 38565934.50286132
- MAE: 4190.934869866732
- RMSE: 6210.147703787835

## Model Selection
The Random Forest Regression model shows the best overall performance with:
- Highest R² Score
- Lowest error metrics
- Good generalization capability
- Robust to outliers

## Feature Importance
Top influential features (Random Forest):
1. Smoker status
2. BMI
3. Age
4. Number of children
5. Region
