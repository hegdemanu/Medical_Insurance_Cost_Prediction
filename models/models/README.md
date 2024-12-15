
```markdown
# Models Directory

## Purpose
This directory stores trained machine learning models in pickle format.

## Model Files
- random_forest_model.pkl: Random Forest Regression model
- xgboost_model.pkl: XGBoost Regression model
- lightgbm_model.pkl: LightGBM Regression model
- linear_regression_model.pkl: Linear Regression model

## Usage
1. Models are automatically saved here after training
2. Use model_training.py's load_model function to load models
3. Models can be versioned with timestamps or version numbers

## Notes
- .gitkeep ensures the directory is tracked
- .pkl files should be added to .gitignore
- Keep model metadata (training date, performance metrics) in docs/
```
