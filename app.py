import time

import numpy as np
import pandas as pd
import pickle
import streamlit as st


st.title('Предсказание на основе модели')
st.text('Введите данные для предсказания')

def load_model():
    with open("model.pickle", "rb") as file:
        model = pickle.load(file)
    return model
    from load_model import load_model

    model = load_model()

st.sidebar.title('ИТ-АКАДЕМИЯ ПРИОРБАНК')
st.sidebar.title('Проект "Отток клиентов"')
st.write("""
Эта модель предсказывает уйдет клиент банка или останется!
""")

def user_input_features():
    Age = st.slider('Возраст', 18, 92, 31)
    Balance = st.slider('Баланс', 0.00, 12544.90, 2000.00)
    NumOfProducts = st.slider('Количество продуктов', 1, 4, 2)
    EstimatedSalary = st.slider('Зарплата', 0.00, 4444.28, 1500.00)
    CreditScore = st.slider('Скоринговый балл', 0, 850, 400)
    data = {'Возраст': Age,
            'Баланс': Balance,
            'Количество продуктов': NumOfProducts,
            'Зарплата': EstimatedSalary,
            'Скоринговый балл': CreditScore,}
    features = pd.DataFrame(data, index=[0])
    return features
input = user_input_features()


if st.button("Предсказать отток клиентов"):
    if input_data:
        prediction = pred(model, input)
        st.write(prediction)
        
      

st.sidebar.info('Курс Diving into Darkness of Data Science.')
st.sidebar.info('Подготовила проект Кругленя А.М.')
