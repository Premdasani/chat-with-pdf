# Chat with PDF

Chat with PDF is a document question-answering web application that allows users to upload PDF files and ask questions based on the document content.
The system extracts text from the uploaded PDF, converts it into embeddings, stores them in a vector database (FAISS), and retrieves the most relevant information to generate answers using a language model.
This helps users quickly understand large documents without reading them completely.


## Features

- Upload PDF documents through an interactive interface
- Ask questions related to the document content
- Retrieve context-based answers from the PDF
- Uses semantic similarity search for better responses
- Efficient document chunking and embedding storage
- Simple Streamlit-based user interface

---

## Tech Stack

Language:
- Python

Libraries and Frameworks:
- Streamlit
- LangChain
- FAISS (Vector Database)
- HuggingFace Embeddings
- OpenAI API

Concepts Used:
- Text extraction from PDF
- Document chunking
- Embedding generation
- Vector similarity search
- Retrieval-based response generation

---

## How the Project Works

The application follows this workflow:

Upload PDF  
→ Extract text from document  
→ Split text into chunks  
→ Generate embeddings  
→ Store embeddings in FAISS  
→ User asks question  
→ Retrieve relevant chunks  
→ Generate response using language model

---

## Project Structure

chat-with-pdf/

app.py                # Main Streamlit application  
embeddings.py         # Embedding generation logic  
utils.py              # Helper functions  
requirements.txt      # Project dependencies  
README.md             # Project documentation

---a

## Installation and Setup

Clone the repository:

git clone https://github.com/Premdasani/chat-with-pdf.git


Move into the project directory:

cd chat-with-pdf


Install dependencies:

pip install -r requirements.txt

---

## Environment Variables Setup

Create a `.env` file inside the project directory and add:

OPENAI_API_KEY=your_api_key_here

---

## Run the Application

Start the Streamlit server:

streamlit run app.py


Then open the application in your browser:

http://localhost:8501

---

## Use Cases

This project can be useful for:

- Understanding research papers quickly
- Extracting information from study material
- Asking questions from textbooks or notes
- Reviewing documentation efficiently
- Working with large PDF files interactively

---

## Future Improvements

Planned enhancements:

- Support multiple PDF uploads
- Add conversation history feature
- Improve user interface design
- Support local LLM models
- Deploy using Docker or cloud platforms

---

## Author

Prem Dasani  
GitHub: https://github.com/Premdasani

---

## Support

If you found this project useful, consider giving it a star on GitHub.
