import streamlit as st

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader


import streamlit as st
import time

st.title("Hi, I am here to tell You about Mikołaj. Go ahead and ask me some questions!")


if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "name_available" not in st.session_state:
    st.session_state.name_available = False

text_input_container = st.empty()
text_input_container.text_input(placeholder='Your name',label="Before we begin, would You mind introducing Yourself?", key="user_name")
if st.session_state.user_name != "":
    text_input_container.empty()
    with st.empty():
        st.write(f"Thanks!")
        time.sleep(1)
        st.empty()


if st.session_state.user_name:
    st.title("Echo Bot")
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        print(st.session_state)
