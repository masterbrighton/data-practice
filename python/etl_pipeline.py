import pandas as pd
import psycopg2
from sqlalchemy import create_engine 

#load CSV with Python
superstore_df = pd.read_csv("datasets/train.csv")

#converting date column
for col in ('Order Date', 'Ship Date'):
    superstore_df[col] = pd.to_datetime(superstore_df[col], dayfirst=True)

#clean data
superstore_df_clean = superstore_df.dropna()

#connecting to database
user = "your_username"
password = "your_password"
host = "localhost"
port = 5432
database = "superstorepsql_db"

#loading data to postgres
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

table_name = "superstorepsql"
superstore_df_clean.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ Data successfully loaded into table '{table_name}' in database '{database}'.")
