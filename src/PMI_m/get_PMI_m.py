import json

def pmi_getter(c_code, tedata_lib):
    """
    Retrieves Manufacturing PMI (Purchasing Managers' Index) data for a specified country.
    
    Args:
        c_code (str): Country code (e.g., 'US', 'CN', 'GB')
        tedata_lib: Library for scraping Trading Economics data
        
    Returns:
        None: Data is exported to Excel file
    """
    # Open and load the JSON file containing country codes mapped to country names
    with open(r"src/T25.json", "r") as countries:
        countries = json.load(countries)
    
    # Scrape PMI data from Trading Economics
    # Note: US uses "business-confidence" endpoint instead of "manufacturing-pmi"
    if c_code != "US":
        scraped = tedata_lib.scrape_chart(url = f"https://tradingeconomics.com/{countries[c_code]}/manufacturing-pmi")
    else:
        scraped = tedata_lib.scrape_chart(url = "https://tradingeconomics.com/united-states/business-confidence")

    # Export the scraped data to an Excel file
    # The data is stored in the "series" attribute of the scraped object
    # Metadata is stored in the "metadata" attribute 
    # Data can be visualized using the "plot_series" method
    try:
        # Export data to Excel file named "mydata.xlsx" in the current working directory
        scraped.export_data(filename = "mydata")
        print(scraped)  # Print information about the scraped object
    except PermissionError:
        # Handle the case when the Excel file is already open
        print("Permission error: You likely have the excel file open")


# Commented out execution code - uncomment to test the function directly
# if __name__ == "__main__":
#     pmi("US")

