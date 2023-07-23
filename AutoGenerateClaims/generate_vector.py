import pickle
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

import pandas as pd

# Load OpenAI token from .env file
import os

articles = {} # key is article id, value is article text
df = pd.read_excel('./cleaned.xlsx')
articles = pd.Series(df['content'].values,index=df['article_id']).to_dict()

# init text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, # you can modify these parameters if you want
    chunk_overlap=150, # you can modify these parameters if you want
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
