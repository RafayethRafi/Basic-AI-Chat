from langchain_openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
import os
import streamlit as st

def get_openai_response(question):
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),temperature=0.5,model="gpt-3.5-turbo-instruct")
    response = llm(question)
    return response


st.set_page_config(page_title="QNA Demo")
st.header("Langchain Application")

input = st.text_input("Enter your question here:")
response = get_openai_response(input)

submit = st.button("Ask Ques")

if submit:
    st.subheader("The response is:")
    st.write(response)