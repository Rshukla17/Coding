import pandas as pd

# Load dataset
data = pd.read_csv('/mnt/data/Simulated Dataset.csv')

# Display basic information
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Preview the dataset
print(data.head())
