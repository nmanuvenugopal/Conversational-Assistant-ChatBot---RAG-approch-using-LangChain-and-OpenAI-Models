# Importing the libraries needed
from PyPDF2 import PdfReader
from langchain.document_loaders.pdf import PyMuPDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores.faiss import FAISS
import streamlit as st
import os


# Autheticating OpenAI APIs
os.environ["OPENAI_API_KEY"] = "sk-proj-"

# Function to read the texts from the PDF
def get_text_from_pdf(pdf_doc):
    text = ""
    for pdf in pdf_doc:
        document = PdfReader(pdf)
        for page in document.pages:
            text += page.extract_text()
    return text

# Function to chunk the text thats read
def get_text_chunk(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text=text)
    return chunks

# Function to convert the text to vectors and saving it in vector stores
def get_vectordata(chunks):
    embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = FAISS.from_texts(embedding=embedding, texts=chunks)
    return vectorstore


# Function for query retrieval
def get_query_conversation_retrieval(vectorstore):
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True)
    retrieval_chain = ConversationalRetrievalChain.from_llm(
        llm = ChatOpenAI(temperature=0, model="gpt-4o"),
        retriever=vectorstore.as_retriever(),
        get_chat_history = lambda h:h,
        memory = memory
    )
    return retrieval_chain


# Designing UI with Streamlit
# All function mentioned above will be called here

user_uploads = st.file_uploader("Upload your PDF files", accept_multiple_files=True)
if user_uploads is not None:
    if st.button("Upload"):
        with st.spinner("Processing"):
            raw_text = get_text_from_pdf(user_uploads)
            chunks = get_text_chunk(raw_text)
            vector_store = get_vectordata(chunks)
            st.session_state.conversation = get_query_conversation_retrieval(vectorstore=vector_store)


# Time to test the finctionality with user questions

if user_query := st.chat_input("Enter your query here"):
    if "conversation" in st.session_state:
        result = st.session_state.conversation({
            "question": user_query,
            "chat_history": st.session_state.get('chat_history', [])
        })
        response = result["answer"]
    else:
        response = "Please upload a document to start a conversation"
    
    with st.chat_message("assistant"):
        st.write(response)





