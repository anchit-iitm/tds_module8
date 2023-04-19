import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Larger Value Checker App
This app checks for the greater value amoung the 2 given values
""")

st.header('User Input Parameters')

def user_input_features():
