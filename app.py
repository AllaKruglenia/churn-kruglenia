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



def main():
    st.title("Прогноз оттока клиентов")
    html_temp = """
    <div style="background-color:white ;padding:10px">
    <h2 style="color:red;text-align:center;">Заполни форму</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

CreditScore = st.slider('Скоринговый балл', 300, 900)

Geography = st.selectbox('География/регион', ['France', 'Germany', 'Spain'])
Geo = int(le1_pik.transform([Geography]))

Gender = st.selectbox('Пол', ['Male', 'Female'])
Gen = int(le_pik.transform([Gender]))

Age = st.slider("Возраст", 10, 95)

Tenure = st.selectbox("Стаж", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15'])

Balance = st.slider("Баланс", 0.00, 250000.00)

NumOfProducts = st.selectbox('Количество продуктов', ['1', '2', '3', '4'])

HasCrCard = st.selectbox("Есть кредитная БПК ?", ['0', '1'])

IsActiveMember = st.selectbox("Активный клиент ?", ['0', '1'])

EstimatedSalary = st.slider("Зарплата", 0.00, 200000.00)


def predict_churn(CreditScore, Age, Balance, NumOfProducts, EstimatedSalary):
    input = np.array([[CreditScore, Age, Balance, NumOfProducts, EstimatedSalary]]).astype(np.float64)
    if option == 'XGBoost':
        prediction = model.predict_proba(input)
        pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    else:
        pred=0.30
        #st.markdown('Наверное, клиент останется в банке, но это не точно да и вообще надо звонить в Битву экстрасенсов.')

    return float(pred)        

   churn_html = """  
              <div style="background-color:#f44336;padding:20px >
               <h2 style="color:red;text-align:center;"> Жаль, но теряем клиента.</h2>
               </div>
            """
    no_churn_html = """  
              <div style="background-color:#94be8d;padding:20px >
               <h2 style="color:green ;text-align:center;"> Ура, клиент остаётся в банке !!!</h2>
               </div>
            """

    if st.button('Сделать прогноз'):
        output = predict_churn(CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
        st.success('Вероятность оттока составляет {}'.format(output))
        st.balloons()

        if output >= 0.5:
            st.markdown(churn_html, unsafe_allow_html= True)

        else:
            st.markdown(no_churn_html, unsafe_allow_html= True)

if __name__=='__main__':
    main()

st.sidebar.info('Курс Diving into Darkness of Data Science.')
st.sidebar.info('Подготовила проект Кругленя А.М.')
