
```python
import pytest
import numpy as np
from src.model_training import (
    split_data, 
    train_linear_regression,
    train_xgboost,
    train_lightgbm,
    train_random_forest
)

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    X = np.random.rand(100, 5)
    y = np.random.rand(100)
    return X, y

def test_split_data(sample_data):
    """Test data splitting functionality."""
    X, y = sample_data
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    assert X_train.shape[0] == y_train.shape[0]
    assert X_test.shape[0] == y_test.shape[0]
    assert len(X) == len(X_train) + len(X_test)

def test_train_linear_regression(sample_data):
    """Test linear regression training."""
    X, y = sample_data
    X_train, _, y_train, _ = split_data(X, y)
    model = train_linear_regression(X_train, y_train)
    assert model is not None

def test_train_random_forest(sample_data):
    """Test random forest training."""
    X, y = sample_data
    X_train, _, y_train, _ = split_data(X, y)
    model = train_random_forest(X_train, y_train)
    assert model is not None
```
