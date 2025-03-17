# to run this app , you need to install the following packages:
# command : python3 -m streamlit run app.py

import streamlit as st
import csv
import time
import seaborn as sns
import plotly.express as px
import warnings
import seaborn as sns
import plotly.graph_objects as go
import numpy as np
import math
import pickle
import pandas as pd
from feature_engine.outliers import ArbitraryOutlierCapper
warnings.filterwarnings("ignore")
pd.options.mode.chained_assignment = None

from appCode import mpswt

st.set_page_config(page_title="Health_Insurance", layout="wide", initial_sidebar_state="expanded")

def explore_page():
   
   
    st.sidebar.header("Model Configuration")  
    age = st.sidebar.number_input("Enter your age",step=1)
    sex_options = ['male', 'female']
    sex = st.sidebar.selectbox("Select your sex", sex_options)

    bmi_text = st.sidebar.text_input("Enter your BMI", value="")
    bmi = float(bmi_text) if bmi_text else None

    Children=st.sidebar.number_input("Enter no of children you have", step=1)
    smoker = st.sidebar.radio("Do you smoke?", ["yes", "no"])

    region = st.sidebar.radio("Select your region", ["northwest", "northeast", "southeast", "southwest"])
    
    
    st.markdown("<h1 style='color:white;'>Health Insurance Prediction Model</h1>", unsafe_allow_html=True)
 
    st.subheader(":violet[Model Settings]")
    st.write(f"Age: {age}")
    st.write(f"Sex: {sex}")
    st.write(f"BMI: {bmi}")
    st.write(f"No of Children: {Children}")
    st.write(f"Smoker: {smoker}")
    st.write(f"Region: {region}")
  
    
    
 
    cols = st.columns(4)
    
    if cols[1].button("Create Prediction"):
        mpswt(age,sex,bmi,Children,smoker,region)
    
 
   

explore_page()
st.markdown('<p style="text-align: center; font-size: 15px; color: #00e3fc;">© 2025 RVCE,Bangalore. All rights reserved.</p>', unsafe_allow_html=True)