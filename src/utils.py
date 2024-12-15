```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def set_plotting_style():
    """Set consistent style for all plots."""
    plt.style.use('seaborn')
    sns.set_palette("husl")

def save_dataframe(df: pd.DataFrame, path: str) -> None:
    """Save DataFrame to CSV file."""
    df.to_csv(path, index=False)

def load_dataframe(path: str) -> pd.DataFrame:
    """Load DataFrame from CSV file."""
    return pd.read_csv(path)

def calculate_statistics(df: pd.DataFrame, column: str) -> dict:
    """Calculate basic statistics for a given column."""
    return {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'std': df[column].std(),
        'min': df[column].min(),
        'max': df[column].max()
    }

def create_datetime_features(date_column: pd.Series) -> pd.DataFrame:
    """Create datetime features from a date column."""
    date_column = pd.to_datetime(date_column)
    return pd.DataFrame({
        'year': date_column.dt.year,
        'month': date_column.dt.month,
        'day': date_column.dt.day,
        'dayofweek': date_column.dt.dayofweek,
        'quarter': date_column.dt.quarter
    })
```
