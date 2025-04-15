import json

def pmi_getter (c_code, tedata_lib):
    with open(r"src\T25.json", "r") as countries:
        countries = json.load(countries)
    

    #This returns a TE_scraper object with the data stored in the "series" attribute.
    if c_code != "US":
        scraped = tedata_lib.scrape_chart(url = f"https://tradingeconomics.com/{countries[c_code]}/manufacturing-pmi")
    else:
        scraped = tedata_lib.scrape_chart(url = "https://tradingeconomics.com/united-states/business-confidence")

    # Metadata is stored in the "metadata" attribute and the series is easily plotted 
    # using the "plot_series" method.
    #  
    try:
        scraped.export_data(filename = "mydata") #Will save to current wd as "my_data.xlsx"
        print(scraped)
    except(PermissionError):
        print("Permission error: You likely have the excel file open")


# if __name__ == "__main__":
#     pmi("US")

