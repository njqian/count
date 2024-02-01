
import streamlit as st
import pandas as pd
import time

st.title("你好！史文震！")
count = 0
empty1 = st.empty()
empty2 = st.empty()
while True:     
    with empty2:
      count += 1 
      st.subheader(count) 
      time.sleep(1)
    empty1.empty()
      
    