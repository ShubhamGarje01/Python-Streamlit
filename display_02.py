import pandas as pd
import numpy as np
import streamlit as st

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
nd = n.reshape(2, 4)

dic = {"name": "Sam",
            "age": 25,
            "city": "Pune"}

#Converting variable into dataframe of streamlit
st.dataframe(a)
st.dataframe(n)
st.dataframe(nd)
st.text(dic) #dict data type cannot convert into dataframe

data = pd.read_csv('D:\\ExcelR_Classes_Data\\Stremalit\\claimants.csv')
st.dataframe(data)#, width=750, height=750)

#when data is not very large we can use tables

st.table(data)
st.table(a)
st.table(n)
st.table(nd)

#write function is the most powerfull in the streamlit

st.write(a)
st.write(n)
st.write(nd)
