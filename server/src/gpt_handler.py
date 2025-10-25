from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from embedding_handler import embedding_model
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from prompt_handler import *
from embedding_handler import embedding_model
import os
import requests

load_dotenv()


# API KEYS
HF_API_KEY = os.getenv("HF_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


# Create chunk of each request
index_name = "careai"
embedding = embedding_model()

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})


# Chat Model
HF_API_URL = "https://router.huggingface.co/v1/chat/completions"

def ask_huggingface(prompt: str, model="openbiollm/medical-llama3-8b", max_tokens=500) -> str:
    """
    Sends a prompt to a Hugging Face chat model and returns the text response.
    """
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return str(data)
            
    except Exception as e:
        print(f"Error calling Hugging Face API: {e}")
        return None


# Connect Huggingface
class connect_Model:
    def __init__(self, model="Qwen/Qwen3-Coder-30B-A3B-Instruct:nebius"):
        self.model = model

    def invoke(self, input_text):
        return {"output_text": ask_huggingface(input_text, model=self.model)}

chatModel = connect_Model()


# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)


# Combine RAG chains
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)
