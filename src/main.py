import tedata as ted
from PMI_m.get_PMI_m import pmi_getter

def main(country):
    pmi = pmi_getter(country)



if __name__ == "__main__":
    main("US")