import json
import pandas as pd

def scraper(indicator, c_code, tedata_lib):
    """
    Retrieves economic indicator data for a specified country.
    
    Args:
        c_code (str): Country code (e.g., 'US', 'CN', 'GB')
        tedata_lib: Library for scraping Trading Economics data
        indicator (string) :The indicator which we want to load 
        
    Returns:
        Scraped: the scraped data
    """
    # Open and load the JSON file containing country codes mapped to country names
    with open(r"src/T25.json", "r") as countries:
        countries = json.load(countries)
    country = countries[c_code]
    # Scrape data from Trading Economics
    scraped = tedata_lib.scrape_chart(url = f"https://tradingeconomics.com/{country}/{indicator}")
    # Note: US uses "business-confidence" endpoint instead of "manufacturing-pmi"
    if c_code == "US" and indicator == "manufacturing-pmi":
        scraped = tedata_lib.scrape_chart(url = "https://tradingeconomics.com/united-states/business-confidence")

    return scraped.series, pd.Series(scraped.metadata)
 