
import pytest
from src.data_preprocessing import load_data, preprocess_data

def test_load_data():
    df = load_data("path/to/test/data.csv")
    assert not df.empty
    assert list(df.columns) == ["age", "sex", "bmi", "children", "smoker", "region", "charges"]
