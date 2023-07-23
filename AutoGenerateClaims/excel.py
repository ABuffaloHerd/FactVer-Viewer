import pandas as pd
import re

# Load the Excel file
df = pd.read_excel('./FactVer1.3.xlsx')

# Filter rows so that i'm working with Electric vehicles and don't gobble all my ram
filter_mask = df['article_id'].astype(str).str.startswith('Electric')

# Compile your regex patterns
rgx = re.compile(r"\\n[\"'],\s")
rgx2 = re.compile(r"[\"'][0-9]+:\s")
rgx3 = re.compile(r"\\n{0,}")
no_newlines = re.compile(r"\\n")
fk_off_leading_1 = re.compile(r"[\"']1:\s")

# Apply the filter to the DataFrame
filtered_df = df[filter_mask]

def clean_the_data(content):
    # Replace '[' and ']' characters
    fixed = content.replace('[', ' ')
    fixed2 = fixed.replace(']', ' ')

    # Split the text into parts
    parts = rgx.split(fixed2)

    # Initialize a list to store cleaned parts
    clean_parts = []

    for part in parts:
        # remove anything that has the keyword 'adsbygoogle'
        if "adsbygoogle" in part: 
            continue

        # Perform replacements
        clean = fk_off_leading_1.sub('', part)
        clean = rgx2.sub('', clean)
        clean = rgx3.sub('', clean)
        clean_parts.append(clean)

    # Join all the cleaned parts with '\n'
    clean_text = '\n'.join(clean_parts)
    return clean_text

filtered_df['content'] = filtered_df['content'].apply(clean_the_data)

# Save the DataFrame to a new Excel file
filtered_df.to_excel('./cleaned.xlsx', index=False)