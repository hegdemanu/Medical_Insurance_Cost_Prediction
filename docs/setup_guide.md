
# Setup Guide

## Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/hegdemanu/Medical_Insurance_Cost_Prediction
   
2.Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3.Install dependencies:
```bash
pip install -r requirements.txt
```
### 2.3 Data Directory

#### data/README.md
```markdown
# Dataset Information

## Data Source
The dataset contains medical insurance cost information...

## File Structure
- insurance.csv: Main dataset file
- synthetic_data.csv: Generated synthetic data for testing

## Data Loading
Use the data_preprocessing.py module to load and preprocess the data.
