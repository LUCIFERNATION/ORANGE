import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

booster = data["model"]

def show_predict_page():
    st.title("Orange Churn Prediction v2022.0 - CHURN99")

    st.write("""### We need some almost correct information to predict the customer's attrition """)

    Last_Disconnect_Time = st.slider("Last Disconnect Time in Days", 0,100,0)
    Maximum_Time_Between_Disconnections  = st.slider("Maximum Time Between Disconnections in Days", 0, 100, 15)
    Minimum_Time_Between_Disconnections = st.slider("Minimum Time Between Disconnections in Days", 0, 100, 15)
    Maximum_Time_Between_Recharges = st.slider("Maximum Time Between Recharges in Days", 0, 100, 10)
    Phone_Topup_Amount = st.slider("Phone Top-up Amount in Days", 0, 1000, 5)
    _4G_Data_Amount = st.slider("Average 4G Data Amount Per Day", 0, 1000, 1)
    The_Last_Day_the_Customer_Made_an_Incoming_Call = st.slider("The Last Day the Customer Made an Incoming Call", 0, 100, 3)
    The_Last_Day_the_Customer_Made_a_Purchase = st.slider("The Last Day the Customer Made a Purchase", 0, 100, 3)
    The_Last_Day_the_Customer_Made_a_Purchase_of_SOS_Credit = st.slider("The Last Day the Customer Made a Purchase of SOS Credit", 0, 1000, 3)
    The_Last_Day_the_Customer_Made_a_Recharge = st.slider("The Last Day the Customer Made a Recharge", 0, 100, 3)
    The_Last_Day_the_Customer_Made_an_Outgoing_Call = st.slider("The Last Day the Customer Made an Outgoing Call", 0, 100, 3)
    Incoming_PutCall_Ratio = st.slider("Incoming Put-Call Ratio", 0, 100, 18)
    st.info(
    "This is an **improved version app** made for the "
    "Orange Telecom [**web apps**](https://www.orange.tn/) "
    "developed by [**Kaïs BHIR**](https://www.linkedin.com/in/ka%C3%AFs-bhir/). Enjoy Predictions!\n\n"
     )
    st.write(
    "The algorithm is well trained on a collection of KPIs and Has an accuracy score of 98%"
     )

    Predict = st.button("Predict with BEST MODEL !")
    if Predict:
        X = np.array([[Last_Disconnect_Time, Maximum_Time_Between_Disconnections, Minimum_Time_Between_Disconnections , 
        Maximum_Time_Between_Recharges , Phone_Topup_Amount , _4G_Data_Amount , The_Last_Day_the_Customer_Made_an_Incoming_Call , 
        The_Last_Day_the_Customer_Made_a_Purchase , The_Last_Day_the_Customer_Made_a_Purchase_of_SOS_Credit , The_Last_Day_the_Customer_Made_a_Recharge , 
        The_Last_Day_the_Customer_Made_an_Outgoing_Call , Incoming_PutCall_Ratio]])
        X = X.astype(float)
        churn = booster.predict((X))
        if churn > 0.5:
            (st.subheader(f"This Orange customer will stay with us !"))
        else: 
            (st.subheader(f"This Orange customer may churn soon enough !"))