from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


def app():   

    df = pd.read_csv('./dataset/covid_19_india_preprocessed.csv')
    # st.write(df.head())

    
    st.dataframe(df) 
    col = list(df.columns)

# **********************scatter plot*********************
    st.subheader('Scatter Plot')
    option_x = st.selectbox(
            'What feature do you want in the x-axis?',
                col,key=1)

    st.write('You selected:', option_x)
    option_y = st.selectbox(
            'What feature do you want in the y-axis?',
                col)
    st.write('You selected:', option_y)

    figs=px.scatter(df,x=option_x,y=option_y)
    st.write(figs)
    

    print(list(df.columns))


# # /**************Line Plot****************/

    
#     st.subheader('Line Plot')
#     line_x='Date'
#     # line_x = st.selectbox(
#     # 'What feature do you want in the x-axis?',
#     #     col)
#     # st.write('You selected:', line_x)
#     line_y = st.selectbox(
#     'What feature do you want in the y-axis?',
#         col,key=2)
#     st.write('You selected:', line_y)

#     chart_data = pd.DataFrame(
#         np.random.randn(40, 2),
#         columns=[line_x, line_y])

#     st.line_chart(chart_data)


#     # pd.DataFrame.plot.line(x=line_x, y=line_y)

# /******************Bar chart **************/

    st.subheader('Bar Chart')
    bar_x = st.selectbox('What feature do you want in the x-axis?',
        col,key=3
    )

    fig_bar=px.histogram(df,x=bar_x)
    

    st.write(fig_bar)
        

 # /**************** Histogram *******************/
    st.subheader('Histogram')
    hist_x = st.selectbox("What feature do you want in the x-axis?",
        col,key=6)
    plt.hist(df[hist_x])
    st.pyplot()
 # /****************  Joint plot (kind='hex')**************** /
    st.subheader('Joint Plot')
    joint_x = st.selectbox("What feature do you want in the x-axis?",
        col,key=11)
    joint_y = st.selectbox("What feature do you want in the y-axis?",
        col,key=12)
    sns.jointplot(x=joint_x, y=joint_y, data=df, height=5)
    st.pyplot()




st.set_option('deprecation.showPyplotGlobalUse', False)
