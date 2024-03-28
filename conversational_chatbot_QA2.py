# importing the environment variables
from dotenv import load_dotenv
load_dotenv()

chat_history = [] # list for storing the chat b/w user and AI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
msg_2_model = """Act as a helpful assistant that has phenomenal language skills
which is used to assist/respond/suggest/clarify/answer/enagage users with their queries.
The response has to be short, easy to grasp and to the point"""
chat_history.append(SystemMessage(content = msg_2_model))

import streamlit as st
# setting up an application using streamlit
st.header('Hi! How can I help you ???')
user_query = st.text_input('Ask me anything')
button = st.button('Answer') # a button which when clicked will return response 

from langchain_openai import ChatOpenAI
chatllm = ChatOpenAI(temperature=0.4)

if 'chat_history' not in st.session_state :
    st.session_state['chat_history'] = chat_history

if button : # if the button is clicked run the model & fetch the response
    st.session_state['chat_history'].append(HumanMessage(content = user_query))
    response = chatllm(st.session_state['chat_history']).content
    st.session_state['chat_history'].append(AIMessage(content=response))
    st.write(response)
    

