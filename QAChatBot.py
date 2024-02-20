# import openai
# importing 
import warnings
warnings.filterwarnings('ignore')
# from langchain_community.llms import OpenAI
from langchain.llms import OpenAI
# from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
# taking environment variables from .env file
load_dotenv()
# Set your OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question):
    llm=OpenAI(
        openai_api_key = openai_api_key,
        model_name='davinci-002', 
        temperature=0.1
        )
    response=llm(question)
    return response
    # response = openai.Completion.create(
    #     engine="davinci-codex",  # You can experiment with different engines
    #     prompt=prompt,
    #     max_tokens=150,
    #     n=1,
    #     stop=None,
    #     temperature=0.7,
    # )
    # return response.choices[0].text.strip()
    
# Streamlit UI
def main():
    st.title("Question-Answering Chatbot")

    # Get user input
    user_input = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        if user_input:
            # Generate answer using OpenAI API
            answer = generate_answer(user_input)

            # Display the answer
            st.text("Answer: " + answer)

if __name__ == "__main__":
    main()
