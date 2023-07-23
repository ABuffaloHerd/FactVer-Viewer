import json
import os
import pickle
import csv

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
    content:list[str] = csv_data[fName]["content"]
    
    print("Processing", file, "with headline", headline)
    
    # context is the 5 biggest chunks of content
    content.sort(key=len, reverse=True)
    context = content[:5]
    
    # print("\n\n====Context:", context, "\nHeadline:", headline, "\n====\n\n")
    # print("\n\n====Headline:", headline, "\nContext:", context, "\n====\n\n")
    # claim = input("Enter a claim: ")
    
    # if claim == "":
    #     print("Program terminated.")
    #     break
    
    vectordb:VectorStore = None
    with open(f'./data/store/{file}', 'rb') as f:
        vectordb = pickle.load(f)
    
    # Generate a "claim" that is made from the content
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm:ChatOpenAI = ChatOpenAI(model_name='gpt-4')

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # ask to "generate a claim from <content>", but the claim must not be longer than 100 tokens
    query = f"###Prompt generate a one sentence claim from {context}###\n\n"
    claim = ""
    try:
        llm_response = qa(query)
        claim = llm_response["result"]
        print("Claim:", llm_response["result"])
    except Exception as err:
        print('Exception occurred. Please try again', str(err))
        continue
    
    if claim == "":
        print("No response from LLM.")
        continue
    
    # Generate embeddings for the claim and the content
    claim_embedding = model.encode(claim, convert_to_tensor=True)
    content_embeddings = model.encode(content, convert_to_tensor=True)
    
    # Calculate cosine similarities
    similarity_scores = util.pytorch_cos_sim(claim_embedding, content_embeddings)[0]
    
    # scored content
    scored_content:dict = {}
    for i in range(len(content)):
        scored_content[content[i]] = float(similarity_scores[i])
    
    # remove duplicates based on key (so if the same sentence appears twice, the one with the lower score is kept)
    scored_content = {k: v for k, v in sorted(scored_content.items(), key=lambda item: item[0])}
    
    # sort by value highest to lowest
    scored_content = {k: v for k, v in sorted(scored_content.items(), key=lambda item: item[1], reverse=True)}
    
    # iterate through scored_content and set item["validity"] to True or False based on the similarity score
    scored_content = {k: {"validity": v > 0.5, "score": v} for k, v in scored_content.items()}
    
    export_data = {
        "headline": headline,
        "claim": claim,
        "scored_content": scored_content
    }
    
    with open(f'./data/out/{fName}_results.json', 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=4)
