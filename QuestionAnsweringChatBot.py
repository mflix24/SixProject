###########  Question Answering ChatBot  ###########


# importing 
import warnings
warnings.filterwarnings('ignore')
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
# taking environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# creating a function to load the OpenAI model and get the response
def get_openai_response(question):
    llm=OpenAI(
        openai_api_key = openai_api_key,
        model_name='davinci-002', 
        temperature=0.6
        )
    response=llm(question)
    return response

# Initializing the streamlit appliacation
st.set_page_config(page_title='Q&A Chatbot')
st.header('Langchain Application')

# Initializing the input text
input=st.text_input('Input: ',key='input')
response=get_openai_response(input)

# submit button creation and 
# if submit button is clicked
submit=st.button('Ask Question')
if submit:
    st.subheader('The response is ')
    st.write(response)


# print('Hi Sidratul Muntaha')



