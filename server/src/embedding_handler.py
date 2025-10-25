from sentence_transformers import SentenceTransformer


def embedding_model():
    Model = SentenceTransformer(r'D:\models\all-MiniLM-L6-v2')
    return Model