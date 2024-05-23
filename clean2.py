import pandas as pd

df = pd.read_excel('cleaned.xlsx')

df.drop(columns=['ID', 'Адрес', 'Дом'], inplace=True)
# df.drop(columns=['ID', 'Дом'], inplace=True)

df['Время до метро (мин)'] = df['Метро'].str.extract('(\d+)').astype(float)

df['Этаж'] = df['Этаж'].str.split('/').str[0].astype(float)

df.drop(columns=['Метро'], inplace=True)

# адрес
# def process_address(address):
#     if 'улица' in address:
#         street = address.split('улица', 1)[-1].strip()
#         if street:
#             return street
#     return None

# df['Адрес'] = df['Адрес'].apply(process_address)

# df.dropna(subset=['Адрес'], inplace=True)

# df = df[~df['Адрес'].str.startswith(',')]

# df['Адрес'] = df['Адрес'].str.replace(r'\b\d+\w*', '')
# df['Адрес'] = df['Адрес'].str.replace(',', '')
# df['Адрес'] = df['Адрес'].str.replace(r'\b\d+\w*|\,', '', regex=True).str.strip()
# unique_streets = df['Адрес'].unique()

# Создание новых столбцов для каждой улицы и заполнение их нулями
# for street in unique_streets:
#     df[street] = 0

# # Заполнение столбцов значениями 1, если адрес содержит улицу
# for index, row in df.iterrows():
#     address = row['Адрес']
#     for street in unique_streets:
#         if street in address:
#             df.at[index, street] = 1
# df.drop(columns=['Адрес'], inplace=True)

# Присвоение номеров улицам в столбце "Адрес"
# streets = df['Адрес'].str.extract(r'([а-яА-Я]+\s?[а-яА-Я]+)').squeeze().unique()
# street_dict = {street: i for i, street in enumerate(streets, 1)}
# df['Адрес'] = df['Адрес'].str.extract(r'([а-яА-Я]+\s?[а-яА-Я]+)').map(lambda x: street_dict.get(x))

print(df.head())

df.to_excel('cleaned2.xlsx', index=False)