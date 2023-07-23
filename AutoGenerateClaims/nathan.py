import json
import os
import pickle
import csv

import pandas as pd

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import VectorStore

from sentence_transformers import SentenceTransformer, util

# Load environment variables 
from dotenv import load_dotenv
load_dotenv()

csv_data = {}

# Load data.csv into csv_data
with open('./data/data.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        # Skip header row
        if row[0] == "article_id": continue

        # add to csv_data
        article_id = row[0].replace(' ', '_').lower()  # First column is the article_id
        csv_data[article_id] = {
            "headline": row[4],  # Fifth is headline
            "content": row[5].split('\n')  # Sixth is content
        }


# Initialize the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

for file in os.listdir('./data/store'):
    # Parse file name to get article id
    fName = file.split('_vectorstore')[0].replace(' ', '_').lower()
    
    # Headline is a string
    headline = csv_data[fName]["headline"]
    
    # Content is a list of strings
    content = csv_data[fName]["content"]
    
    print("Processing", file, "with headline", headline)
    
    vectordb:VectorStore = None
    with open(f'./data/store/{file}', 'rb') as f:
        vectordb = pickle.load(f)
    
    # Generate a "claim" that is made from the content
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm:ChatOpenAI = ChatOpenAI(model_name='gpt-4')

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # ask to "generate 100 claims from <content>", but the claim must not be longer than 100 tokens
    query = f"###Prompt generate a claim from {content[:len(content) // 2]}. The claim must not be longer than 50 tokens.###\n"
    res = ""
    try:
        llm_response = qa(query)
        claim = llm_response["result"]
        # claim = json.loads(res)["claims"]
        print("Response:", llm_response)
        print("Claim:", claim)
        # print("Claim:", llm_response["result"])
    except Exception as err:
        print('Exception occurred. ', str(err))
        continue
    
    if res == "":
        print("No response from LLM.")
        continue
    
    # # for each claim, generate a score and embed it
    # for claim in claims:
    # Generate embeddings for the claim and the content
    claim_embedding = model.encode(claim, convert_to_tensor=True)
    content_embeddings = model.encode(content, convert_to_tensor=True)
    
    # Calculate cosine similarities
    similarity_scores = util.pytorch_cos_sim(claim_embedding, content_embeddings)[0]
    
    # write scores to file
    with open(f'./data/scores/{fName}_scores.txt', 'w', encoding='utf-8') as f:
        for i in range(len(content)):
            f.write(f"{i+1}. {content[i]} (similarity score: {similarity_scores[i]})\n")
    
    scored_content:dict = {}
    for i in range(len(content)):
        scored_content[content[i]] = float(similarity_scores[i])
    
    # remove duplicates based on key (so if the same sentence appears twice, the one with the lower score is kept)
    scored_content = {k: v for k, v in sorted(scored_content.items(), key=lambda item: item[0])}
    
    # sort by value highest to lowest
    scored_content = {k: v for k, v in sorted(scored_content.items(), key=lambda item: item[1], reverse=True)}
    
    with open(f'./data/scores/{fName}_scores.json', 'w', encoding='utf-8') as f:
        json.dump(scored_content, f, indent=4)
    
    # show top 6
    # print("Top 6 similar content:")
    # for i in range(6):
    #     print(f"{i+1}. {list(scored_content.keys())[i]} (similarity score: {list(scored_content.values())[i]})")

    # Put the claim and the top 6 similar content into a json file for parsing later.
    with open(f'./data/out/{fName}_generated.json', 'w', encoding='utf-8') as f:
        data = {"claim": claim, "content": list(scored_content.keys())[0:6] }
        json.dump(data, f)

        break
