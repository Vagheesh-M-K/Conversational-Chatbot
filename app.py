from dotenv import load_dotenv
load_dotenv() # this functions loads all the variables from .env file

from langchain_openai import OpenAI
llm = OpenAI(temperature=0.6)

def get_output(query) : 
    response = llm(query)
    return response

import streamlit as st
st.header('Very Basic Query Answerer')
input = st.text_input("Ask me anything")
button = st.button('Get Answer')
if button :
    st.write(get_output(input))
    

