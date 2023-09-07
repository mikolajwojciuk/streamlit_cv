import streamlit as st
import logging

logging.info("Importing openai embeddings")
from langchain.embeddings.openai import OpenAIEmbeddings
logging.info("Importing text splitter")
from langchain.text_splitter import CharacterTextSplitter
logging.info("Importings FAISS")
from langchain.vectorstores import FAISS
logging.info("Importing text loader")
from langchain.document_loaders import TextLoader
st.write("Hello, it's Mikołaj!")
