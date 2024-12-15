
```python
from setuptools import setup, find_packages

setup(
    name="medical-insurance-prediction",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=1.5.3',
        'numpy>=1.23.5',
        'scikit-learn>=1.2.2',
        'seaborn>=0.12.2',
        'matplotlib>=3.7.1',
        'xgboost>=1.7.5',
        'lightgbm>=3.3.5',
        'scipy>=1.10.1',
    ],
    author="[Manu]",
    author_email="[hegdemanu22@gmail.com]",
    description="A machine learning project to predict medical insurance costs",
    keywords="machine learning, insurance, prediction",
    url="https://github.com/hegdemanu/medical_insurance_Cost_prediction",
)
```
Repository Setup Instructions

Initial Setup:

``` bash
###Create repository structure
mkdir -p medical-insurance-prediction/{data,models,notebooks,src,tests,docs}
cd medical-insurance-prediction
# Initialize git
git init

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```
Git Setup:

```bash
# Initial commit
git add .
git commit -m "Initial commit"

# Add remote repository
git remote add origin https://github.com/hegdemanu/Medical_Insurance_Cost_Prediction.git
git branch -M main
git push -u origin main
```
