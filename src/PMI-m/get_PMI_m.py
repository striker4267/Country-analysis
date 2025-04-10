import requests, json
from extract import extract
import tedata as ted

# def pmi (country):
#     with open(r"src\PMI-m\pmi_links.json", "r") as pmiLinks:
#         links = json.load(pmiLinks)
    
#     link = links[country]
#     url = link

#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         PMI_value = extract(country, data)
#         print(PMI_value)
#     else:
#         print(f"error: {response.status_code}")


# if __name__ == "__main__":
#     pmi("US")

#This returns a TE_scraper object with the data stored in the "series" attribute.
scraped = ted.scrape_chart(url = "https://tradingeconomics.com/united-states/manufacturing-pmi")

# Metadata is stored in the "metadata" attribute and the series is easily plotted 
# using the "plot_series" method.
#  
try:
    scraped.export_data(filename = "mydata") #Will save to current wd as "my_data.xlsx"
except(PermissionError):
    print("Permission error: You likely have the excel file open")