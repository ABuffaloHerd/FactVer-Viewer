import pickle
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import numpy as np

from dotenv import load_dotenv
load_dotenv()

# Load embeddings
embeddings = OpenAIEmbeddings()

# Compute cosine similarity to pick the most similar chunks
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def generate_claim():
    # Ask user for a claim
    claim = input("Enter your claim: ")

    # Compute the embedding of the claim
    # claim_embedding = embeddings.compute(claim)
    claim_embedding = embeddings.embed_query(claim)

    # Load the article IDs
    df = pd.read_excel('./cleaned.xlsx')
    article_ids = df['article_id'].values

    # Iterate through vectorstores and find the most similar chunks
    for article_id in article_ids:
        # Load the vectorstore
        with open(f'./{article_id}_vectorstore.pkl', 'rb') as f:
            vectorstore = pickle.load(f)
            
        # Query the vectorstore for the most similar chunks
        most_similar_chunks = vectorstore.max_marginal_relevance_search_by_vector(claim_embedding, k=6)

        # Get the vectors of the most similar chunks
        most_similar_chunk_vectors = [chunk.vector for chunk in most_similar_chunks]

        # Compute the cosine similarity between the claim and the most similar chunks
        similarities = [cosine_similarity(claim_embedding, chunk_vector) for chunk_vector in most_similar_chunk_vectors]
        
        # Pick six most similar chunks
        ranked_chunks = sorted(zip(most_similar_chunks, similarities), key=lambda x: x[1], reverse=True)
        for x in range(6):
            print(ranked_chunks[x][0].page_content)
            print(ranked_chunks[x][1])
            print("")

        # x = 0
        # for chunk in most_similar_chunks:
        #     print(chunk.page_content)
        #     x += 1

        #     if(x == 6):
        #         break

generate_claim()