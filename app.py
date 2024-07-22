# import streamlit as st



# api_key = os.getenv("OPENAI_API_KEY")




# # Dummy credentials
# USERNAME = "admin"
# PASSWORD = "123456"

# #

# def add_bg_from_url():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: #F2D4D6;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Streamlit app
# st.set_page_config(page_title="ASKSIDEWAYS", page_icon=":bar_chart:")
# add_bg_from_url()
# st.title("ASKSIDEWAYS")

# # Login form
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if not st.session_state.logged_in:
#     st.subheader("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         if username == USERNAME and password == PASSWORD:
#             st.session_state.logged_in = True
#             st.success("Login successful!")
#             st.experimental_rerun()
#         else:
#             st.error("Invalid username or password")
# else:
#     st.
 



import streamlit as st
import pandas as pd
import os
from pandasai.llm import OpenAI
from pandasai import SmartDataframe

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(api_token=api_key)
# Dummy credentials
USERNAME = "admin"
PASSWORD = "123456"

def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F2D4D6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Streamlit app
st.set_page_config(page_title="ASKSIDEWAYS", page_icon=":bar_chart:")
add_bg_from_url()
st.title("ASKSIDEWAYS")

# Login form
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
else:
    st.subheader("Upload and Display CSV")

    # Upload CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    text = st.text_input("Enter your question regarding the data")

    if uploaded_file is not None:
        if text is not None:
            df = pd.read_csv(uploaded_file)

            if st.button("Submit Question"):
                sdf = SmartDataframe(df, config={"llm": llm})
                sdf.chat(text)
                print(sdf.chat(text))


