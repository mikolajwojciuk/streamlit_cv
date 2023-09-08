import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import time
import os

st.title("Hi, I am here to tell You about Mikołaj. Go ahead and ask me some questions!")



if 'faiss_db' not in st.session_state:
    st.session_state.faiss_db = FAISS.load_local('faiss_index', OpenAIEmbeddings())

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = load_qa_chain(llm=OpenAI(model_name='gpt-3.5-turbo',temperature=0.1),chain_type='stuff')

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "name_available" not in st.session_state:
    st.session_state.name_available = True

text_input_container = st.empty()
text_input_container.text_input(placeholder='Your name',label="Before we begin, would You mind introducing Yourself?", key="user_name")
if st.session_state.user_name != "":
    text_input_container.empty()
    if st.session_state.name_available:
        st.session_state.name_available = False
        with st.empty():
            st.write(f"Thanks!")
            time.sleep(1)
            st.empty()
        
if st.session_state.user_name:
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # React to user input
    if query := st.chat_input("Question"):
        # Display user message in chat message container
        st.chat_message("user").markdown(query)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": query})
        #response = f"Echo: {prompt}"
        #Generate response
        relevant_docs = st.session_state.faiss_db.similarity_search(query)
        response = st.session_state.qa_chain.run(input_documents=relevant_docs, question = query)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        print(st.session_state)
