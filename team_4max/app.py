import streamlit as st
from  multiapp import MultiApp
from apps import home, predict, about

app = MultiApp()

st.title('''Covid 19 Diagnosis and Analysis App'''
    
)

app.add_app("Covid Diagnosis", predict.app)
app.add_app("Covid EDA on India", home.app)
app.add_app("About", about.app)

app.run()