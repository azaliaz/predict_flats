import streamlit as st
import pandas as pd
import pickle

@st.cache_data()
def load_model():
    with open('trained_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

st.title('Предсказание стоимости квартиры')
st.write('Введите параметры квартиры:')

rooms = st.slider('Количество комнат', min_value=1, max_value=3)
new_building = st.radio('Новостройка', ('Да', 'Нет'))
area = st.number_input('Площадь (в квадратных метрах)', min_value=1.0, max_value=400.0, step=1.0)
parking = st.radio('Парковка', ('Есть', 'Нет'))
renovation = st.radio('Ремонт', ('Без ремонта', 'Косметический', 'Евроремонт', 'Дизайнерский'))
delivery_year = st.number_input('Год сдачи дома', min_value=1950, max_value=2030, step=1)
ceiling_height = st.number_input('Высота потолков (в метрах)', min_value=1.0, max_value=5.0, step=0.1)
floor = st.number_input('Этаж', min_value=1, max_value=50, step=1)
distance_to_metro = st.number_input('Время до метро (в минутах)', min_value=1, max_value=50, step=1)

new_building = 1 if new_building == 'Да' else 0
parking = 1 if parking == 'Есть' else 0
remont_mapping = {'Без ремонта': 0, 'Косметический': 1, 'Евроремонт': 2, 'Дизайнерский': 2}
renovation = remont_mapping.get(renovation, 0)

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

predicted_price = model.predict(input_data)

st.markdown("<h2>Предсказанная стоимость квартиры:</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size:20px; color:rgb(112, 215, 52)'>{}</h3>".format(predicted_price[0]), unsafe_allow_html=True)