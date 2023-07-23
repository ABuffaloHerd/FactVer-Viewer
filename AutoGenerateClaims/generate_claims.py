import pickle
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

# Load embeddings
embeddings = OpenAIEmbeddings()

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
        # most_similar_chunks = vectorstore.search(claim_embedding, k=10, search_type="mmr")
        most_similar_chunks = vectorstore.max_marginal_relevance_search_by_vector(claim_embedding, k=6)
        
        # Prints 6 of the most similar chunks from each article
        x = 0
        for chunk in most_similar_chunks:
            print(chunk.page_content)
            x += 1

            if(x == 6):
                break

generate_claim()