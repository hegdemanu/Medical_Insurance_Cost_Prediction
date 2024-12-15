from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import lightgbm as ltb
import pickle

def split_data(X, y, test_size=0.33, random_state=42):
    """Split the data into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_linear_regression(X_train, y_train):
    """Train Linear Regression model."""
    model = LinearRegression()
    return model.fit(X_train, y_train)

def train_xgboost(X_train, y_train, random_state=0):
    """Train XGBoost model."""
    model = xgb.XGBRegressor(random_state=random_state)
    return model.fit(X_train, y_train)

def train_lightgbm(X_train, y_train):
    """Train LightGBM model."""
    model = ltb.LGBMRegressor()
    return model.fit(X_train, y_train)

def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    """Train Random Forest model."""
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
    return model.fit(X_train, y_train)

def save_model(model, filename):
    """Save the trained model."""
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

def load_model(filename):
    """Load a trained model."""
    with open(filename, 'rb') as file:
        return pickle.load(file)
