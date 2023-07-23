import pickle
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# openai.api_base = "https://openrouter.ai/api/v1"

from dotenv import load_dotenv
load_dotenv()

import pandas as pd

# Load OpenAI token from .env file
import os
# openai_token = os.getenv('OPENAI_TOKEN')

# load articles into this dictionary

articles = {} # key is article id, value is article text
df = pd.read_excel('./cleaned.xlsx')
articles = pd.Series(df['content'].values,index=df['article_id']).to_dict()

# init text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # you can modify these parameters if you want
    chunk_overlap=200, # you can modify these parameters if you want
    length_function=len,
)

# initialize embeddings
embeddings = OpenAIEmbeddings()

# iterate through all articles and generate article text
for article_id, article_text in articles.items():
    # generate chunks from article text
    chunks = text_splitter.split_text(text=article_text)
    
    # generate store name from article id
    store_name = f"{article_id}_vectorstore"
    
    # generate vectorstore from chunks
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    
    # write vectorstore to disk
    with open(f'./{store_name}.pkl', 'wb') as f:
        pickle.dump(vectorstore, f)

# Ask user for a claim
claim = input("Enter your claim: ")

# Compute the embedding of the claim
claim_embedding = embeddings.compute(claim)

# Iterate through vectorstores and find the most similar chunks
for article_id in articles.keys():
    # Load the vectorstore
    with open(f'./{article_id}_vectorstore.pkl', 'rb') as f:
        vectorstore = pickle.load(f)
        
    # Query the vectorstore for the most similar chunks
    most_similar_chunks = vectorstore.query(claim_embedding)
    
    # Print the most similar chunks
    print(f"In article {article_id}, the most similar chunks to the claim are:")
    for chunk in most_similar_chunks:
        print(chunk)