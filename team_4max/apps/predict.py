import streamlit as st
import pickle
import numpy as np

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def app():
    df = pd.read_csv('./dataset/corona_tested_individuals_preprocessed.csv')

    X = df.drop(['corona_result'], axis = 1)
    Y = df['corona_result']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 66)
    logmodel = LogisticRegression()
    logmodel.fit(X_train, y_train)

    y_pred = logmodel.predict(X_test)

    accuracy_lr = logmodel.score(X_test, y_test)

    st.warning('Select 1 for Yes and 0 for No')
    cough = st.radio(
        "Do you have cough?",
        (1, 0))
    fever = st.radio(
        "Do you have fever?",
        (1, 0))
    sore_throat = st.radio(
        "Do you have a sore throat?",
        (1, 0))
    shortness_of_breath = st.radio(
        "Are you suffering from shortness of breath?",
        (1, 0))
    head_ache = st.radio(
        "Do you have a head ache?",
        (1, 0))
    age_60_and_above = st.radio(
        "Are you above the age of 60?",
        (1, 0))
    test_indication = st.radio(
        "Have you been tested positive before?",
        (1, 0))

    if st.button("Predict the diagnosis"):
        st.write("The accuracy of our model's diagnosis is:",accuracy_lr)
        output = logmodel.predict([[cough,fever,sore_throat,shortness_of_breath,
                             head_ache,age_60_and_above,test_indication]])
        st.success('The diagnosis is  {}'.format(output))

        if output == 1:
            st.warning("You are Covid positive")
        elif output == 0:
            st.success("You are Covid negative")
    
