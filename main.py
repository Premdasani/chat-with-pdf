import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.llms import Ollama

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate


def get_pdf_text(pdf_docs):
    text = ""

    for pdf in pdf_docs:
        try:
            pdf.seek(0)
            pdf_reader = PdfReader(pdf, strict=False)

            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        except Exception as e:
            st.error(f"Error reading PDF {pdf.name}: {e}")

    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return text_splitter.split_text(text)


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversation_chain():
    prompt = PromptTemplate(
        template="""
        Answer the question using ONLY the provided context.
        If the answer is not available in the context, say:
        "Answer is not available in the context provided."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """,
        input_variables=["context", "question"]
    )

    llm = Ollama(model="llama3.2:1b")

    chain = (
        {
            "context": lambda x: x["context"],
            "question": lambda x: x["question"]
        }
        | prompt
        | llm
    )

    return chain


def user_input(user_question):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    new_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = new_db.similarity_search(user_question, k=3)
    context_text = "\n\n".join(doc.page_content for doc in docs)

    chain = get_conversation_chain()

    response = chain.invoke({
        "context": context_text,
        "question": user_question
    })

    st.write(response)


def main():
    st.set_page_config(page_title="Chat with PDF", page_icon="📚")
    st.header("Chat with multiple PDF files")

    user_question = st.text_input("Ask a question about your PDFs:")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader(
            "Upload PDFs and click Process",
            accept_multiple_files=True
        )

        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vectorstore(text_chunks)
                st.success("Processing complete. You can now ask questions.")


if __name__ == "__main__":
    main()
