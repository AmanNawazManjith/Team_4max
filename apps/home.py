from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.arrow import Data
import plotly.figure_factory as ff
from bokeh.plotting import figure
from PIL import Image


def app():   

    image = Image.open('./images/covid_forecasting.jpg')
    st.image(image, caption='A simple covid analysis application')
    df = pd.read_csv('./dataset/covid_19_india_preprocessed.csv')
    # st.write(df.head())
    st.subheader('A preview of the Covid Dataset we selected')

    
    st.dataframe(df) 
    col = list(df.columns)
    st.title('EDA (Exploratory Data Analysis)')
 
    st.subheader('Scatter Plot')
    st.caption('The following are the most affected places in India')
    col1,col2= st.columns(2)

    with col1:
        st.caption("Maharashtra")
        df = pd.DataFrame(
        np.random.randn(1000, 2)/[50,50]+[20.59, 78.96],
        columns=['latitude', 'longitude'])
        st.map(df,zoom=7)

    with col2:
        
        st.caption("Kerala")
        df1 = pd.DataFrame(
        np.random.randn(1000, 2)/[50,50]+[10.85,76.27],
        columns=['latitude', 'longitude'])
        st.map(df1,zoom=7)


    col3,col4= st.columns(2)

    with col3:
        st.caption("Andhra Pradesh")
        df = pd.DataFrame(
        np.random.randn(1000, 2)/[50,50]+[15.91, 79.74],
        columns=['latitude', 'longitude'])
        st.map(df,zoom=7)

    with col4:
        st.caption("Odisha")
        df1 = pd.DataFrame(
        np.random.randn(1000, 2)/[50,50]+[20.95,85.09],
        columns=['latitude', 'longitude'])
        st.map(df1,zoom=7)
    


 

    st.header('Line Chart')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Deaths', 'Cured', 'Confirmed'])

    st.line_chart(chart_data)

 

    st.subheader('Bar Chart')
    bar_x = st.selectbox('What feature do you want in the x-axis?',
        col,key=2
    )
    bar_y = st.selectbox('What feature do you want in the y-axis?',
        col,key=3
    )
    bar_z = st.selectbox('What feature do you want in the z-axis?',
        col,key=4
    )
 



    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=[bar_x, bar_y, bar_z])

    st.bar_chart(chart_data)
        

  
    st.subheader('Plotly')
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = [x1, x2, x3]

    group_labels = ['Confirmed', 'Cured', 'Deaths']

    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1,.25,.5]
    )
    st.plotly_chart(fig)
 




st.set_option('deprecation.showPyplotGlobalUse', False)
