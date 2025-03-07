import streamlit as st
import pandas as pd

st.title('this is a title editted')
st.header('This is a header')
st.markdown('deploy this thing via github')

df = pd.read_csv('./test_file.csv')
st.area_chart(df)
