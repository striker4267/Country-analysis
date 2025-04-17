import json
import pandas as pd

def scraper(indicator, c_code, tedata_lib):
    """
    Retrieves economic indicator data for a specified country.
    
    Args:
        indicator (str): The economic indicator to download (e.g., 'manufacturing-pmi')
        c_code (str): Country code (e.g., 'US', 'CN', 'GB')
        tedata_lib: Library for scraping Trading Economics data
        
    Returns:
        tuple: (data_series, metadata) containing the scraped data and its metadata
    """
    # Open and load the JSON file containing country codes mapped to country names
    # This mapping is needed to construct proper URLs for Trading Economics
    with open(r"src/T25.json", "r") as countries:
        countries = json.load(countries)
    
    # Get the URL-friendly country name from the country code
    country = countries[c_code]
    
    # Construct the URL and scrape data from Trading Economics
    scraped = tedata_lib.scrape_chart(url = f"https://tradingeconomics.com/{country}/{indicator}")
    
    # Special case handling for US manufacturing PMI
    # The US uses "business-confidence" endpoint instead of "manufacturing-pmi"
    if c_code == "US" and indicator == "manufacturing-pmi":
        scraped = tedata_lib.scrape_chart(url = "https://tradingeconomics.com/united-states/business-confidence")

    # Return both the data series and metadata as separate objects
    # The series contains the actual economic data points
    # The metadata contains information about the data source, units, etc.
    return scraped.series, pd.Series(scraped.metadata)