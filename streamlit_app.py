import streamlit as st
import pandas as pd

st.write("""
        # Hello
        """)

data = pd.read_csv("IMDB Dataset.csv")

st.line_chart(data)