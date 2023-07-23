import pandas as pd
import json
import os

# All the data is stored in the out folder as a json file.
# iterate through entire folder and parse all the json files to pandas dataframe
# and then concat all the dataframes into one dataframe
# and then save it as an excel file.

# path to the folder where all the json files are stored
PATH = './data/out/'

master_df = pd.DataFrame()

for filename in os.listdir(PATH):
    if filename.endswith('_results.json'):
        with open(os.path.join(PATH, filename), 'r') as f:
            data = json.load(f)

            # convert the 'scored_content' dictionary to a list of tuples
            scored_content = [(k, v['validity'], v['score']) for k, v in data['scored_content'].items()]

            # sort the list by score in descending order
            scored_content.sort(key=lambda x: x[2], reverse=True)

            # Now, we can create a list of dictionaries in which each dictionary represents a row in the desired DataFrame.
            # Each dictionary includes 'headline', 'claim', 'content', 'validity', and 'score'
            title = filename[:-13].capitalize()
            data_list = [{'article_id': title, 'Claim': data['claim'], 'Evidence': content, 'TFN': "T" if validity else "F", 'score': score} for content, validity, score in scored_content]

            # Take the top 6 scored content
            data_list = data_list[:6]
            
            # create a dataframe from the list of dictionaries
            df = pd.DataFrame(data_list)
            # print(df.head())

            # # write to file for debugging
            # with open('dataframe.txt', 'w') as f:
            #     f.write(df.to_string())

            # print("file written")
            # Add the dataframe to the master dataframe
            master_df = pd.concat([master_df, df], ignore_index=True)

            # Export the dataframe to excel file
            master_df.to_excel('final_claims.xlsx', index=False)

print("Three months of data generated in less than a day. Was it really worth it?")