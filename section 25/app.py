import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


from  langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama.llms import OllamaLLM

from langchain_core.prompts import  ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

# google_llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
gemma_llm = OllamaLLM(model="gemma3:4b")




prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that helps people find information."),
        ("user", "Question: {question}")
    ])


st.title("demo - gemma3b ")

chain = prompt | gemma_llm | StrOutputParser()


question =st.chat_input("what question do you have?")
if question:
    # question = st.chat_input("what question do you have?")
    response = chain.invoke({"question": question})
    st.chat_message("human").write(question)
    st.chat_message("ai").write(response)
