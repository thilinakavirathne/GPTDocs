#pip install streamlit langchain openai faiss-cpu tiktoken

import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile

from chatbot import Chatbot  # Import the modified Chatbot class

user_api_key = st.sidebar.text_input(
    label="##############################", 
    placeholder="##########################, sk-",
    type="password")

uploaded_file = st.sidebar.file_uploader("upload", type="csv")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
    data = loader.load()

    embeddings = OpenAIEmbeddings()
    vectors = FAISS.from_documents(data, embeddings)

    # Use the modified Chatbot class
    chatbot = Chatbot(model_name='text-davinci-003', temperature=0.0, vectors=vectors)

    # Container for chat history
    response_container = st.container()
    # Container for user's text input
    container = st.container()

    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! anything about " + uploaded_file.name]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey!"]

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            # Use the modified chatbot's method
            output = chatbot.conversational_chat(user_input)

            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                st.write(st.session_state["past"][i], key=str(i) + '_user', style="text-align:center")
                st.write(st.session_state["generated"][i], key=str(i), style="text-align:center")
