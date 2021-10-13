import streamlit as st
from  multiapp import MultiApp
from apps import home, predict, classify

app = MultiApp()

st.markdown('''#This is the starting of the app'''
    
)

app.add_app("Home -> 1st Page", home.app)
app.add_app("Predict -> 2nd Page", predict.app)
app.add_app("Clasify -> 3rd Page", classify.app)

app.run()