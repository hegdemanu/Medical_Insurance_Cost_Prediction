
```python
import pytest
import pandas as pd
import numpy as np
from src.data_preprocessing import load_data, preprocess_data, check_missing_values, check_duplicates

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'age': [25, 30, 35, 40],
        'sex': ['male', 'female', 'male', 'female'],
        'bmi': [22.1, 23.4, 24.5, 25.6],
        'children': [0, 1, 2, 1],
        'smoker': ['yes', 'no', 'no', 'yes'],
        'region': ['northeast', 'northwest', 'southeast', 'southwest'],
        'charges': [1000, 2000, 3000, 4000]
    })

def test_check_missing_values(sample_data):
    """Test missing values check functionality."""
    missing_values = check_missing_values(sample_data)
    assert all(missing_values == 0)

def test_check_duplicates(sample_data):
    """Test duplicate detection functionality."""
    duplicates = check_duplicates(sample_data)
    assert len(duplicates) == 0

def test_preprocess_data(sample_data):
    """Test data preprocessing functionality."""
    preprocessor = preprocess_data(sample_data)
    assert preprocessor is not None
```
