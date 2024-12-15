import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Define data loading and preprocessing
def prepare_data():
    # Create synthetic data for demonstration
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'age': np.random.randint(18, 65, n_samples),
        'sex': np.random.choice(['male', 'female'], n_samples),
        'bmi': np.random.normal(30, 6, n_samples),
        'children': np.random.randint(0, 5, n_samples),
        'smoker': np.random.choice(['yes', 'no'], n_samples),
        'region': np.random.choice(['northeast', 'northwest', 'southeast', 'southwest'], n_samples)
    }
    
    # Generate target variable (medical charges)
    # Base charge
    charges = 5000 + np.random.normal(0, 1000, n_samples)
    
    # Age factor
    charges += data['age'] * 100
    
    # BMI factor
    charges += np.where(data['bmi'] > 30, (data['bmi'] - 30) * 500, 0)
    
    # Smoker factor
    charges += np.where(np.array(data['smoker']) == 'yes', 15000, 0)
    
    # Children factor
    charges += np.array(data['children']) * 2000
    
    # Add some noise
    charges += np.random.normal(0, 1000, n_samples)
    
    data['charges'] = charges
    
    return pd.DataFrame(data)

def create_and_save_model():
    # Load data
    df = prepare_data()
    
    # Split features and target
    X = df.drop('charges', axis=1)
    y = df['charges']
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create preprocessing steps
    numeric_features = ['age', 'bmi', 'children']
    categorical_features = ['sex', 'smoker', 'region']
    
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first', sparse=False)
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Create pipeline
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=100,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            random_state=42
        ))
    ])
    
    # Fit the model
    model.fit(X_train, y_train)
    
    # Save the model
    with open('models/RFmodel.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Return model and test data for verification
    return model, X_test, y_test

if __name__ == "__main__":
    # Train and save model
    model, X_test, y_test = create_and_save_model()
    
    # Verify model performance
    score = model.score(X_test, y_test)
    print(f"Model R² score: {score:.4f}")
