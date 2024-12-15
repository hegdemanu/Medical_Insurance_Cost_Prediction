
```markdown
# Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager
- git

## Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/[username]/medical-insurance-prediction.git
cd medical-insurance-prediction
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development Setup

1. Install development dependencies:
```bash
pip install pytest pytest-cov black isort flake8
```

2. Set up pre-commit hooks (optional):
```bash
pip install pre-commit
pre-commit install
```

## Running Tests
```bash
pytest tests/
```

## Code Style
- Use Black for formatting: `black .`
- Use isort for import sorting: `isort .`
- Use flake8 for linting: `flake8 .`

## Building Documentation
```bash
sphinx-build -b html docs/ docs/_build/html
```

## Model Training
1. Place your data in the data/ directory
2. Run the training script:
```bash
python src/model_training.py
```

## Deployment
1. Models are saved in the models/ directory
2. Use the saved models for predictions:
```python
from src.model_training import load_model
model = load_model('models/random_forest_model.pkl')
```
```
