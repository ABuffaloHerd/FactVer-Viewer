import pandas as pd

df = pd.read_excel('./final_claims_tfn_verified.xlsx')

for index, row in df.iterrows():
    claim = row['Claim']
    evidence = row['Evidence']
    
    print("Claim: \n", claim)
    print("")
    print("Evidence: \n", evidence)
    print("")
    print("TFN: ", row['TFN'])

    response = input("T/F/N: ")

    if response == 's':
        continue
    
    # When using iterrows, it actually creates a copy of the row, so we need to use loc to update the original df
    if len(response) > 0:
        if response[0].lower() == 'f':
            df.loc[index, 'TFN'] = 'F'
        elif response[0].lower() == 'n':
            df.loc[index, 'TFN'] = 'N'
        else:
            df.loc[index, 'TFN'] = 'T'
    else:
        df.loc[index, 'TFN'] = 'T'

    reason = input("Reason: ")
    if len(reason) > 0:
        df.loc[index, 'Reason'] = reason
    elif reason == 'c':
        df.loc[index, 'Reason'] = df.loc[index, 'Evidence']
        print("Copied evidence as reason")


    print("")
    print("")
    print("")

    df.to_excel('./final_claims_tfn_verified.xlsx')