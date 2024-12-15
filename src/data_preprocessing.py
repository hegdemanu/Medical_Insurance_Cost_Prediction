import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data(file_path):
    """Load the medical insurance dataset."""
    return pd.read_csv(file_path)

def check_missing_values(df):
    """Check for missing values in the dataset."""
    return df.isnull().sum()

def check_duplicates(df):
    """Check and remove duplicate entries."""
    duplicates = df.duplicated(keep=False)
    return df[duplicates]

def preprocess_data(df):
    """Preprocess the data with numerical and categorical transformations."""
    numerical_columns = ['age', 'bmi', 'children']
    categorical_columns = ['sex', 'smoker', 'region']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', "passthrough", numerical_columns),
            ('cat', OneHotEncoder(sparse_output=False, drop="if_binary"), 
             categorical_columns)
        ])
    
    return preprocessor

def create_synthetic_data(num_samples=5000):
    """Create synthetic data for testing the model."""
    age = np.random.randint(18, 65, size=num_samples)
    sex = np.random.choice(['male', 'female'], size=num_samples)
    smoker = np.random.choice(['yes', 'no'], size=num_samples)
    bmi = np.random.normal(30, 6, size=num_samples)
    children = np.random.randint(0, 5, size=num_samples)
    region = np.random.choice(['northeast', 'northwest', 'southeast', 'southwest'], 
                            size=num_samples)
    
    return pd.DataFrame({
        'age': age,
        'sex': sex,
        'smoker': smoker,
        'BMI': bmi,
        'children': children,
        'region': region
    })
