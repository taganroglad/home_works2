import pandas as pd

# Загрузка данных из файла CSV
df = pd.read_csv('updated_fifa_s2.csv')

print(df.isnull().sum())
# Заполнение пропущенных значений в столбце 'Club' строкой 'Unknown'
df['Club'] = df['Club'].fillna('Unknown')

# Заполнение пропущенных значений в столбце 'Value' средним значением
mean_value = df['Value'].mean()
df['Value'] = df['Value'].fillna(mean_value)
