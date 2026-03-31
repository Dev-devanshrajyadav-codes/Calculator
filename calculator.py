# streamlit run filename.py
from random import choice

import streamlit as st 

st.title("Simple Calculator")
st.subheader("Enter two number and select an opreation to perform")
# st . markdown("Enter two number and select an opreation")

c1,c2 = st.columns(2)
fnum=c1.number_input("Enter a frist number", value=0)
snum=c2.number_input("Enter a second number", value=0)

opreation = ["ADD","SUB","MUL","DIV"]
choice = st.radio("select an operation", opreation)

button = st.button("calculator")

result = 0 
if button:
    if choice == "ADD":
        result = fnum+snum
    if choice == "SUB":
        result = fnum-snum
    if choice == "MUL":
        result = fnum*snum
    if choice == "DIV":
        result = fnum/snum
    
st.success(f"Result:{result}")
    
st.snow()