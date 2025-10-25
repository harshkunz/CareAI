from dotenv import load_dotenv
import os
import requests
from sentence_transformers import SentenceTransformer

load_dotenv()


HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


# Online Hugging Face Model 

def get_embeddings(texts):
    """
        Get embedding vectors for a list of texts using Hugging Face Inference API.
        Recommended only if you don't want to use a local model.
    """
    if isinstance(texts, str):
        texts = [texts]     # convert single string to list

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": texts}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()      # returns list of embedding vectors
    except Exception as e:
        print(f"Embedding error: {e}")
        return None


# local model

def get_local_model(model_path: str = r"D:\models\all-MiniLM-L6-v2") -> SentenceTransformer:
    """
        Loads a local SentenceTransformer model and returns it.
    """
    return SentenceTransformer(model_path)
