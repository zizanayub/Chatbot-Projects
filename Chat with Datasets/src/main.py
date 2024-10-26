import pandas as pd
import streamlit as st
from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_ollama import ChatOllama


## Streamlit Web App Configuration
st.set_page_config(
    page_title = "DF Chat",
    page_icon="💬",
    layout="centered"
)


def read_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)
    


##Stream Page title
st.title("🤖 DataFrame Chatbot")


##initialize chat history in streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


