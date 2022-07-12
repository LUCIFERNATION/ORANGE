import streamlit as st
import pandas as pd
from awesome_streamlit import experiments as ste
from PIL import Image
image = Image.open('orange.png')


# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

from predict_page import show_predict_page
from explore_page import show_explore_page
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


# Hashage
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():
    """CHURN99.ai : Orange Customer Attrition Prediction"""

    st.title("WELCOME TO CHURN99.ai !")
    
    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.title("Check out our TOP 3 Services :")
        st.header("FOR ATHLETES - The Flex Service : ")
        st.info(
    "Flex is a platform that provides you with live lessons, "
    "a large library of on-demand videos, qualified coaches for a better private coaching experience and  "
    "nutrition experts for a healthy lifestyle, check it out now [**FLEX**](https://flexfitness.online/). Enjoy Flexing!\n\n"
     )
        st.header("FOR STUDENTS - The Kademia Service : ")
        st.info(
    "Kademia is a Tunisian startup that offers an educational service  "
    "to support students in their learning journey,  "
    "check it out now [**KADEMIA SERVICE**](https://kademia.tn/). Enjoy Studying!\n\n"
     )
        st.header("FOR CINEPHILES - The Cineday Service : ")
        st.info(
    "If you are an Orange mobile customer and a cinema enthusiast, take advantage "
    "every Thursday of a free cinema ticket for 1 ticket purchased, at Pathé, at the same screening,  "
    "with friends, as a couple or as a family! check it out now [**CINEDAY**](https://www.orange.tn/services-pratiques/cineday). Enjoy Watching!\n\n"
     )

        






    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))


                task = st.selectbox("What is it that you wanna do exactly?",["Predict Orange Customer Churn","Visualize Data","Members"])
                if task == "Predict Orange Customer Churn":
                    show_predict_page()
                elif task == "Visualize Data": 
                    show_explore_page()
                elif task == "Members":
                    st.subheader("User Members")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")





    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu now to login")



if __name__ == '__main__':
    main()