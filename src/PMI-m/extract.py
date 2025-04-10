

def extract(country, data):
    if country == "US":
        return data["series"]["docs"][0]["value"][-1]
    elif country == "CN":
        for series in data["series"]:
            if series["series_name"] == "Manufacturing Purchasing Managers' Index":
                return series["value"][-1]
    
