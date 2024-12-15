import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle
import os

def generate_synthetic_insurance_data(n_samples=1500):
    """Generate synthetic insurance data that mimics real-world patterns."""
    np.random.seed(42)
    
    data = {
        'age': np.random.randint(18, 65, n_samples),
        'sex': np.random.choice(['male', 'female'], n_samples),
        'bmi': np.random.normal(26, 5, n_samples).clip(16, 53),
        'children': np.random.randint(0, 6, n_samples),
        'smoker': np.random.choice(['yes', 'no'], n_samples, p=[0.2, 0.8]),
        'region': np.random.choice(['northeast', 'northwest', 'southeast', 'southwest'], n_samples)
    }
    
    # Generate realistic insurance charges
    charges = 5000 + np.zeros(n_samples)
    
    # Age factor
    charges += data['age'] * 250
    
    # BMI factor (exponential increase for BMI > 30)
    bmi_factor = np.where(data['bmi'] > 30, 
                         np.exp((data['bmi'] - 30) * 0.1) * 1000, 
                         data['bmi'] * 100)
    charges += bmi_factor
    
    # Smoker factor (significant increase)
    charges += np.where(np.array(data['smoker']) == 'yes', 20000 + np.random.normal(0, 5000, n_samples), 0)
    
    # Children factor
    charges += data['children'] * 2000
    
    # Region factor
    region_factors = {
        'northeast': 1.2,
        'northwest': 1.1,
        'southeast': 0.9,
        'southwest': 1.0
    }
    region_multiplier = np.array([region_factors[r] for r in data['region']])
    charges *= region_multiplier
    
    # Add some random variation
    charges += np.random.normal(0, charges * 0.1)
    
    # Ensure charges are positive and reasonable
    charges = np.clip(charges, 1000, 63000)
    
    data['charges'] = charges
    return pd.DataFrame(data)

def create_model_pipeline():
    """Create a preprocessing and model pipeline."""
    numeric_features = ['age', 'bmi', 'children']
    categorical_features = ['sex', 'smoker', 'region']
    
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first', sparse=False)
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        ))
    ])
    
    return model

def train_and_save_model():
    """Train the model and save it as a pickle file."""
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Generate synthetic data
    print("Generating synthetic insurance data...")
    df = generate_synthetic_insurance_data()
    
    # Split features and target
    X = df.drop('charges', axis=1)
    y = df['charges']
    
    # Split into train and test sets
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train model
    print("Training model...")
    model = create_model_pipeline()
    model.fit(X_train, y_train)
    
    # Evaluate model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"Model R² score on training data: {train_score:.4f}")
    print(f"Model R² score on test data: {test_score:.4f}")
    
    # Save the model
    print("Saving model...")
    with open('models/RFmodel.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved as 'models/RFmodel.pkl'")
    
    # Return model and test data for verification
    return model, X_test, y_test

if __name__ == "__main__":
    model, X_test, y_test = train_and_save_model()
    
    # Example prediction
    sample_data = pd.DataFrame({
        'age': [40],
        'sex': ['male'],
        'bmi': [28.5],
        'children': [2],
        'smoker': ['no'],
        'region': ['northeast']
    })
    
    prediction = model.predict(sample_data)
    print(f"\nExample prediction for sample data:")
    print(f"Predicted insurance cost: ${prediction[0]:,.2f}")
