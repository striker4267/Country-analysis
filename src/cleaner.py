import pandas as pd

def clean(file_path):

    #TODO: more sophisticated data cleaning

    df = pd.read_csv(file_path)

    cleaned_df = df.dropna()

    cleaned_df.to_csv(file_path, index=False)