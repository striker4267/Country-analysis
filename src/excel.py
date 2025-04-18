import pandas as pd
import os
import glob


data_dir = "economic_data"

def make_excel(c_code):
    with pd.ExcelWriter(f"{c_code}_economic_data.xlsx", engine="openpyxl") as writer:

        #get all the csv files for that countries data
        csv_files = [ f for f in glob.glob(os.path.join(data_dir, "*.csv")) if "metadata" not in f and f"{c_code}" in f] 

        for csv_file in csv_files:

            basename = os.path.basename(csv_file)
            filename = os.path.splitext(basename)[0]
            indicator = filename.split("_")[1]

            df = pd.read_csv(csv_file, index_col=0, parse_dates=True)

            sheet_name = f"{c_code}_{indicator}"

            df.to_excel(writer, sheet_name=sheet_name)
        
        print(f"Successfully combined data into {c_code}_economic_data.xlsx ")
