import streamlit as st
import pandas as pd
import numpy as np


def input_excel(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        
        return df
    else:
        raise FileNotFoundError("No file uploaded")




##initialize our streamlit app

st.set_page_config(page_title="Excel")

st.header("File Uploader")

uploaded_file = st.file_uploader("Choose a excel file...", type=["csv","xlsx","xls"])

if uploaded_file is not None:
    df = input_excel(uploaded_file)
    

submit=st.button("Submit")

if submit:

    st.write("Display Result")
    a = df["DPD"].value_counts()

    df["DPD"] = df["DPD"].map(lambda x: a[x] if a[x] > 1 else x)
    res=df.iloc[:,2:]

    st.write(res)