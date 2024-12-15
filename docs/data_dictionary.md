```markdown
# Data Dictionary

## Feature Descriptions

### Primary Features
1. age
   - Type: Integer
   - Description: Age of primary beneficiary
   - Range: 18-64 years
   - Units: Years

2. sex
   - Type: String
   - Description: Gender of insurance contractor
   - Values: male, female
   - Encoding: One-hot encoded in preprocessing

3. bmi
   - Type: Float
   - Description: Body mass index
   - Range: Typically 15-50
   - Units: kg/m²

4. children
   - Type: Integer
   - Description: Number of children covered by insurance
   - Range: 0-5
   - Notes: Dependents covered by insurance

5. smoker
   - Type: String
   - Description: Smoking status
   - Values: yes, no
   - Encoding: Binary encoded in preprocessing

6. region
   - Type: String
   - Description: Beneficiary's residential area
   - Values: northeast, northwest, southeast, southwest
   - Encoding: One-hot encoded in preprocessing

### Target Variable
7. charges
   - Type: Float
   - Description: Individual medical costs billed by insurance
   - Units: USD
   - Range: Varies significantly
```
