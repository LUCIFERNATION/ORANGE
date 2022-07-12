from sklearn import datasets
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, HTML
from PIL import Image
import plotly.figure_factory as ff

def clv_function(x):
    if 0 < x < 100:
        return 'New to Orange Tunisia'
    if 100 < x < 260:
        return 'Between 5 and 10 years Service User'
    if 260 < x < 302:
        return 'Old school Service User'
    else:
        return 'Never Consistant with SIM Cards'
@st.cache
def load_data():
    dataset = pd.read_csv("churn.csv")
    df = dataset[["FLAG", "LIFE_TIME", "MONTANT_DATA", "MONTANT_RECHARGE", "MONTANT_SOS"]]
    df = df[df["MONTANT_RECHARGE"].notnull()]
    df = df.dropna()

    df['LIFE_TIME'] = df['LIFE_TIME'].apply(clv_function)
    
    df = df.rename({"FLAG": "CHURNED"}, axis=1)
    df = df.rename({"LIFE_TIME": "Customer lifetime value"}, axis=1)
    df = df.rename({"MONTANT_DATA": "4G Data Usage Per Month"}, axis=1)
    df = df.rename({"MONTANT_RECHARGE": "Average Recharge Amount Per Month"}, axis=1)
    df = df.rename({"MONTANT_SOS": "Average SOS Amount Per Month"}, axis=1)
    return df

df = load_data()

def show_explore_page():
    st.title("CHURN99 APP")

    st.write(
        """
    ### Orange Customer Prediction Beta Version v2022.1.88.d
    """
    )

    data = df["Customer lifetime value"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Customer Lifetime Values into 4 categories of Orange Customers""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Customer Churn Rate Per Year at Orange (Almost 4%)
    """
    )
    image = Image.open('churn_rate.JPG')
    st.image(image, caption='CHURN RATE AT ORANGE TUNISIA')
    
    #data = df.groupby(["CHURNED"])["Average Recharge Amount Per Month"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    st.write(
        """
    #### Mean Recharge Amout Based On CHURNED Customers
    """
    )

    data = df.groupby(["4G Data Usage Per Month"])["Average SOS Amount Per Month"].mean().sort_values(ascending=True)
    st.area_chart(data)