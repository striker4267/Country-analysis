import requests, json


def pmi (country):
    with open(r"src\PMI\pmi_links.json", "r") as pmiLinks:
        links = json.load(pmiLinks)
    
    link = links[country]
    url = link

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"error: {response.status_code}")


if __name__ == "__main__":
    pmi("US")