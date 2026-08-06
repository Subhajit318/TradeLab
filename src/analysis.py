import pandas as pd

#df = pd.read_csv("data/RELIANCE.csv")
df = pd.read_csv("data/RELIANCE.csv", skiprows=2)

print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
print(df.describe())