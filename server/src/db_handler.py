import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore
from src.llm_handler import _


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)


# required fields

extracted_data = _(data='_path_')
filter_data = _(extracted_data)

text_chunks = _()
Model = _()


# create vectors

index_name = "careai"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension=384, 
        metric= "cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)


# update vectors

class SentenceTransformerEmbeddings:
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return [e.tolist() for e in embeddings]  

    def embed_query(self, text):
        embedding = self.model.encode(text, show_progress_bar=False)
        return embedding.tolist() 

embedding = SentenceTransformerEmbeddings(Model)


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embedding
)