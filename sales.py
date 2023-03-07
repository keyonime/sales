# -*- coding: utf-8 -*-
"""Sales.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S8PKkh2787uPLsP4ffWFZA6U2TfWYG5I
"""

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Sales**!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0, 200, 10)
    Radio = st.sidebar.slider('Radio', 0, 100, 10)
    Newspaper = st.sidebar.slider('Newspaper', 0, 100, 10)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

dfdata = pd.read_csv('Adversiting.csv')
dfdata = dfdata.drop(['Unnamed: 0'],axis=1)
X = dfdata.drop(['Sales'],axis=1)
Y = dfdata.Sales

clf = LinearRegression()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(dfdata.target_names)

st.subheader('Prediction')
st.write(dfdata.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
