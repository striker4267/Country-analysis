import pandas as pd
import os
import json
from data_scraper import scraper
from sanitize_filename import sanitize_filename

def get_data(c_code,tedata_lib):
    # create a directory for the csv files if it does not already exist 
    output_dir = "economic_data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # with open("src/indicators.json") as indicators:
    #     indicators_dict = json.load(indicators)
    
    # Uncomment to test
    with open("src/indicators_TEST.json") as indicators:
        indicators_dict = json.load(indicators)

    for indicator_key, indicator_value in indicators_dict.items():
        try:
            print(f"downloading {indicator_value} for {c_code} ...") 

            scraped, metadata = scraper(indicator_value, c_code, tedata_lib)

            data_series = scraped.series


            filename = sanitize_filename(f"{c_code}_{indicator_key}")
            csv_path = os.path.join(output_dir, f"{filename}.csv")

            data_series.to_csv(csv_path)

            #Also save metadata

            metadata_path = os.path.join(output_dir, f"{filename}_metadata.csv")
            metadata.to_csv(metadata_path)

            print(f"saved successfully {csv_path}")
        
        except:
            print(f"Error downloading {indicator_key} for {c_code}")
            continue