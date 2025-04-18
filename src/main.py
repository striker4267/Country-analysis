import tedata as ted
import string
import pandas as pd
import os
import json
from data_getter import get_data
from excel import make_excel


def main(country = "ALL"):
    """
    Main entry point for the economic data scraper application.
    
    Args:
        country (str): Country code to retrieve data for, or "ALL" to process all countries
                      Default is "ALL"
    
    Returns:
        None: Data is exported to CSV files via the get_data function
    """
    
    if country == "ALL":
        # If "ALL" is specified, download data for all countries in T25.json
        with open("src/T25.json", "r") as countries:
            country_dict = json.load(countries)

        # Loop through each country and get its economic data
        # NOTE: There's a bug here - should be country, not country.key
        for country_code in country_dict:
            get_data(country_code, ted) 
            make_excel(country_code)    
    else:
        # Download data for just the specified country
        get_data(country, ted)
        make_excel(country)

if __name__ == "__main__":
    # When script is run directly, download data for Great Britain (GB)
    # This can be modified to download data for any specific country
    main("GB")