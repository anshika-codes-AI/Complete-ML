import streamlit as st
import pandas as pd
st.title("Streamlit text input")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello ! {name}")

age = st.slider("select your age: ",0,100,25)
st.write(f"Your age is {age}.")

## File upload 
uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)