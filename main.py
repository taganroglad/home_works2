import pandas as pd

# Загрузка данных из файла CSV
df = pd.read_csv('fifa_s2.csv')

# Заполнение пропущенных значений в столбце 'Nationality' строкой 'Unknown'
df['Nationality'] = df['Nationality'].fillna('Unknown')

# Заполнение пропущенных значений в столбце 'Club' строкой 'Unknown'
df['Club'] = df['Club'].fillna('Unknown')

# Заполнение пропущенных значений в столбце 'Value' средним значением
mean_value = df['Value'].mean()
df['Value'] = df['Value'].fillna(mean_value)

# Сохранение обновленных данных в том же файле CSV
df.to_csv('fifa_s2.csv', index=False)
