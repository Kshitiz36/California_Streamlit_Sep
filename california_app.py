import numpy as np
import joblib
import streamlit as st

obj=joblib.load('california.joblib')
model=obj['model']
cols=obj['columns']

st.title('california app')
In=[]

for i in cols:
    v=st.number_input(f'Enter the {i} value:')
    In.append(v)
if st.button('click'):
    out=model.predict([In])
    st.success(f'The media house value is : {out}')

