import pandas as pd
import pickle

# Загрузка обученной модели
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Запрос ввода параметров квартиры от пользователя
print("Введите параметры квартиры:")
rooms = int(input("Количество комнат: "))
new_building = int(input("Новостройка (1 - да, 0 - нет): "))
area = float(input("Площадь (в квадратных метрах): "))
parking = int(input("Парковка (1 - есть, 0 - нет): "))
renovation = int(input("Ремонт (1 - сделан, 0 - не сделан): "))
delivery_year = int(input("Год сдачи: "))
ceiling_height = float(input("Высота потолков (в метрах): "))
floor = int(input("Этаж: "))
distance_to_metro = float(input("Время до метро (в минутах): "))

# Создание DataFrame с введенными параметрами
input_data = pd.DataFrame({
    'Количество комнат': [rooms],
    'Новостройка': [new_building],
    'Площадь': [area],
    'Парковка': [parking],
    'Ремонт': [renovation],
    'Срок сдачи': [delivery_year],
    'Высота потолков, м': [ceiling_height],
    'Этаж': [floor],
    'Время до метро (мин)': [distance_to_metro]
})

# Предсказание стоимости квартиры
predicted_price = model.predict(input_data)

print("Предсказанная стоимость квартиры:", predicted_price[0])
