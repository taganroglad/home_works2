
import pandas as pd
df = pd.read_csv('fifa_s2.csv')
print(df.isnull().sum())
