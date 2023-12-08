import streamlit as st
import pickle as pkl
import numpy as np

class_list = {'0': 'Negative', '1': 'Positive', '2': 'Neutral'}
with open('ec_vsfc.pkl', 'rb') as file:
  encoder = pkl.load(file)

st.title('Sentiment Analysis')

text = st.text_input('Enter text')

if text is not None:
  
