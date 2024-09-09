from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


class VectorRepository:
    def __init__(self):
        load_dotenv(dotenv_path='/config/ai/ai.env')

    def get_retriever(self, query: str):
        embedding = OpenAIEmbeddings(model='text-embedding-3-large', openai_api_key=os.getenv('OPENAI_API_KEY'))
        PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
        index_name = 'inflearn-lectures'
        database = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embedding)
        retriever = database.as_retriever(search_kwargs={'k': 4})
        return retriever.get_relevant_documents(query)
