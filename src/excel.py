import pandas as pd
import os
import glob


data_dir = "economic_data"
output_dir = "combined_economic_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def make_excel(c_code):
    try:
        with pd.ExcelWriter(os.path.join(output_dir,f"{c_code}_economic_data.xlsx"), engine="openpyxl") as writer:

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
    except Exception as e:
        print(f"Error creating Excel file for {c_code}: {e}")

if __name__ == "__main__":
    make_excel("GB")