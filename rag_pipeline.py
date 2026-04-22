from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline

from transformers import pipeline


def create_vector_store(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)

    return vector_store


def get_qa_chain(vector_store):
    pipe = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_length=512
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    retriever = vector_store.as_retriever()

    def qa_chain(query):
        docs = retriever.invoke(query)   # ✅ FIXED LINE
        context = " ".join([doc.page_content for doc in docs])

        prompt = f"""
        You are an AI assistant. Answer clearly and concisely.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        
        result = llm.invoke(prompt)
        return result

    return qa_chain