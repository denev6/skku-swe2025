import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_data(db_query: str):
    pass


def create_documents(data, chunk_size: int, chunk_overlap: int):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    docs = []
    for text in data:
        chunks = text_splitter.split_text(text)
        for chunk in chunks:
            doc = Document(page_content=chunk)
            docs.append(doc)
    return docs


def embed(encoder, faiss_index, db_query):
    data = load_data(db_query)
    docs = create_documents(data, chunk_size=1000, chunk_overlap=100)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Embedding vectors on {device}...")
    hf_embeddings = HuggingFaceEmbeddings(
        model_name=encoder, model_kwargs={"device": device}
    )
    faiss_index = FAISS.from_documents(docs, hf_embeddings)
    faiss_index.save_local(folder_path=faiss_index)
    print(f"FAISS index saved to folder: {faiss_index}")
