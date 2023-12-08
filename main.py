import streamlit as st
import pickle as pkl
import numpy as np

class_list = {'0': 'Negative', '1': 'Positive', '2': 'Neutral'}

st.title('Sentiment Analysis')

text = st.text_input('Enter text')

if text is not None:
  
