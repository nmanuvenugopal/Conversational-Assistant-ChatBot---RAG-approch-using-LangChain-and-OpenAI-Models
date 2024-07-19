# PDF-Conversational-Assistant--RAG-approch-using-LangChain-and-OpenAI-Models
PDF Conversational Assistant- RAG approch using LangChain and OpenAI Models

## Overview
This project provides a web-based application that leverages the LangChain and OpenAI libraries to facilitate document-based question-answering. Users can upload PDF documents, which are processed to extract text, split into chunks, converted into vectors, and stored in a vector database. The application uses a conversational model to answer user queries based on the content of the uploaded documents. The entire application is built using Streamlit for a simple and interactive user interface.

## Libraries Used
1. PyPDF2: For extracting text from PDF documents.
2. LangChain: A suite of tools for handling documents, text splitting, embeddings, and conversational models.
3. PyMuPDFLoader and PyPDFLoader: Loaders for reading PDFs.
4. RecursiveCharacterTextSplitter: Splits text into manageable chunks.
5. OpenAIEmbeddings: Converts text into vector embeddings using OpenAI's models.
6. ChatOpenAI: Provides conversational AI models.
7. ConversationalRetrievalChain: Facilitates conversation retrieval based on document embeddings.
8. FAISS: Efficiently stores and retrieves vector embeddings.
9. Streamlit: For building the web application interface.
10. OS: For handling environment variables.

## Functionality
Authenticate OpenAI API:

1. Set up your OpenAI API key to use OpenAI's models.
2. Read Text from PDF: get_text_from_pdf(pdf_doc): Reads and extracts text from the uploaded PDF files.
3. Chunk Text: get_text_chunk(text): Splits the extracted text into chunks to manage processing and storage.
4. Convert Text to Vectors: get_vectordata(chunks): Converts text chunks into vector embeddings using OpenAI's embedding model and stores them in a FAISS vector store.
5. Setup Conversational Retrieval: get_query_conversation_retrieval(vectorstore): Sets up a conversational retrieval chain with a memory component to handle user queries based on the vector store.
6. Streamlit UI: Users can upload PDF files via the file uploader.
7. On clicking the "Upload" button, the uploaded PDFs are processed: text is extracted, chunked, and converted into vectors. A conversational chain is then initialized.
8. Users can enter queries, which are answered by the conversational AI based on the content of the uploaded documents.

## Usage
1. Upload Documents: Use the file uploader in the Streamlit app to upload one or more PDF files.
2. Process Documents: After uploading, click the "Upload" button to process the documents. The text from the PDFs is extracted, chunked, and converted into a format suitable for querying.
3. Ask Questions: Enter a query in the chat input field to receive answers based on the content of the uploaded documents.

# Images 
![image](https://github.com/user-attachments/assets/13e9b47b-4391-4dbc-a7db-d8a20fede884)



![image](https://github.com/user-attachments/assets/2104fb8a-116a-490a-8084-cc5d6cad7b8d)



![image](https://github.com/user-attachments/assets/418309f7-b48d-4ba4-8e6e-824788314f42)



