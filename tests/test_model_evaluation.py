
```python
import pytest
import numpy as np
from src.model_evaluation import calculate_metrics

@pytest.fixture
def sample_predictions():
    """Create sample predictions for testing."""
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
    return y_true, y_pred

def test_calculate_metrics(sample_predictions):
    """Test metrics calculation functionality."""
    y_true, y_pred = sample_predictions
    metrics = calculate_metrics(y_true, y_pred)
    
    assert 'MSE' in metrics
    assert 'R2 Score' in metrics
    assert 'MAE' in metrics
    assert 'RMSE' in metrics
    assert all(value >= 0 for value in metrics.values())
```
