from dotenv import load_dotenv
import os
import requests
from sentence_transformers import SentenceTransformer

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


# online HuggingFace Model

def get_embeddings(texts):
    """
    Get embedding vectors for a list of texts using Hugging Face API.
    """
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": texts}
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None


# local Model

def embedding_model():
    Model = SentenceTransformer(r'D:\models\all-MiniLM-L6-v2')
    return Model