import os
import json
from data_scraper import scraper
from sanitize_filename import sanitize_filename
from cleaner import clean

def get_data(c_code, tedata_lib):
    """
    Main function to retrieve various economic indicators for a specified country.
    
    Args:
        c_code (str): Country code (e.g., 'US', 'CN', 'GB')
        tedata_lib: Library for scraping Trading Economics data
        
    Returns:
        None: Data is exported to CSV files in the 'economic_data' directory
    """
    # Create a directory for the CSV files if it doesn't already exist
    # This ensures we have a designated place to store all the downloaded data
    output_dir = "economic_data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Uncommented in production to use the full set of indicators
    with open("src/indicators.json") as indicators:
        indicators_dict = json.load(indicators)
    
    #Uncomment to test
    # with open("src/indicators_TEST.json") as indicators:
    #     indicators_dict = json.load(indicators)

    # Loop through each indicator and try to download its data
    for indicator_key, indicator_value in indicators_dict.items():
        try:
            # Log the current download operation to track progress
            print(f"downloading {indicator_value} for {c_code} ...") 

            # Call the scraper function to get the data and metadata
            data_series, metadata = scraper(indicator_value, c_code, tedata_lib)

            # Create a safe filename using the country code and indicator key
            filename = sanitize_filename(f"{c_code}_{indicator_key}")
            csv_path = os.path.join(output_dir, f"{filename}.csv")

            # Save the actual economic data to a CSV file
            data_series.to_csv(csv_path)

            # Also save the metadata to a separate CSV file
            # This includes information like data source, last update time, etc.
            metadata_path = os.path.join(output_dir, f"{filename}_metadata.csv")
            metadata.to_csv(metadata_path)

            clean(csv_path)
            clean(metadata_path)

            # Log successful download
            print(f"saved successfully {csv_path}")
        
        except:
            # Log errors for troubleshooting but continue with other indicators
            # This ensures one failed download doesn't stop the entire process
            print(f"Error downloading {indicator_key} for {c_code}")
            continue