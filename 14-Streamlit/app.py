import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## Dispaly a simple text
st.write("This is a simple text")

## create a simple dataframe
df = pd.DataFrame(
    {
        'first coloumn':[1,2,3,4],
        'second coloumn':[10,20,30,40]
    }
)

## Display the dataframe
st.write("Hey! Here's the dataframe")
st.write(df)

##create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns = ['a','b','c']
)

st.line_chart(chart_data)