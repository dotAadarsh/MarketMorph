import streamlit as st
from openai import AzureOpenAI
import numpy as np

AZURE_API_KEY = st.secrets["AZURE_API_KEY"]
ADA_002_AZURE_API_VERSION = st.secrets["ADA_002_AZURE_API_VERSION"]
AZURE_API_ENDPOINT = st.secrets["AZURE_API_ENDPOINT"]

client = AzureOpenAI(
  api_key = AZURE_API_KEY, 
  api_version = ADA_002_AZURE_API_VERSION,
  azure_endpoint = AZURE_API_ENDPOINT
)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def generate_embeddings(text, model="text-embedding-ada-002-southindia"):
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def search_docs(user_query, texts, embeddings, top_n=5):
    user_query_embedding = generate_embeddings(
        user_query,
        model="text-embedding-ada-002-southindia"
    )
    similarities = np.array([cosine_similarity(embedding, user_query_embedding) for embedding in embeddings])
    

    sorted_indices = np.argsort(similarities)[::-1]
    top_indices = sorted_indices[:top_n]
    top_similarities = similarities[top_indices]
    top_texts = [texts[idx] for idx in top_indices]
    top_embeddings = [embeddings[idx] for idx in top_indices]

    return top_texts
