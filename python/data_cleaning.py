import pandas as pd

#load csv
superstore = pd.read_csv("datasets/train.csv")

#show first rows
print(superstore.head(20))

#check missing values
print(superstore.isnull().sum())

#convert date columns
for col in ('Order Date', 'Ship Date'):
    superstore[col] = pd.to_datetime(superstore[col], dayfirst=True)

#save new CSV
superstore.to_csv("datasets/superstore_clean.csv", index=False)