import tedata as ted
import string
import pandas as pd
import os
import json
from data_getter import get_data


def main(country = "ALL"):
    
    if country == "ALL":
        with open("src/T25.json", "r") as countries:
            country_dict = json.load(countries)

        for country in country_dict:
            get_data(country.key, ted)     
    else:
        get_data(country, ted)

if __name__ == "__main__":
    main("GB")