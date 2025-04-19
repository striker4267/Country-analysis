import openpyxl.utils
import pandas as pd  # Import the pandas library for data manipulation
import os  # Import the os module for operating system related tasks
import glob  # Import the glob module for finding files matching a pattern
import openpyxl

# Define the directory where the economic data CSV files are located
data_dir = "economic_data"
# Define the directory where the combined Excel files will be saved
output_dir = "combined_economic_data"

# Check if the output directory exists, and create it if it doesn't
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define a function to create an Excel file containing combined economic data for a specific country code
def make_excel(c_code):
    try:
        # Create an Excel writer object using pandas to write to an Excel file
        # The file will be named based on the country code and saved in the output directory
        # The 'openpyxl' engine is used for writing .xlsx files
        with pd.ExcelWriter(os.path.join(output_dir, f"{c_code}_economic_data.xlsx"), engine="openpyxl") as writer:

            # Get all the CSV files in the data directory that:
            # 1. Do not contain "metadata" in their filename
            # 2. Contain the specified country code (c_code) in their filename
            csv_files = [
                f
                for f in glob.glob(os.path.join(data_dir, "*.csv"))
                if "metadata" not in f and f"{c_code}" in f
            ]

            # Iterate through each of the identified CSV files
            for csv_file in csv_files:
                # Extract the base filename from the full file path
                basename = os.path.basename(csv_file)
                # Split the base filename to remove the ".csv" extension
                filename = os.path.splitext(basename)[0]
                # Split the filename by "_" and assume the second part is the indicator name
                indicator = filename.split("_")[1]

                # Read the CSV file into a pandas DataFrame
                # Set the first column (index 0) as the index of the DataFrame
                # Attempt to parse date-like strings in the CSV into datetime objects
                df = pd.read_csv(csv_file, index_col=0, parse_dates=True)

                # Create a sheet name for the Excel file using the country code and indicator
                sheet_name = f"{c_code}_{indicator}"

                # Write the DataFrame to the Excel file under the generated sheet name
                df.to_excel(writer, sheet_name=sheet_name)

                worksheet = writer.sheets[sheet_name]
                # Alters the lengths of the columns
                for idx, col in enumerate(df.columns, start=0):
                    column_letter = openpyxl.utils.get_column_letter(idx + 1)
                    max_length = max(df[col].astype(str).map(len).max(), len(col))
                    adjusted_width = max_length + 2  # Add a bit of padding
                    worksheet.column_dimensions[column_letter].width = adjusted_width

        # Print a success message indicating that the data has been combined into the Excel file
        print(f"Successfully combined data into {c_code}_economic_data.xlsx ")
    except Exception as e:
        # If any error occurs during the process, print an error message including the exception
        print(f"Error creating Excel file for {c_code}: {e}")

# This block ensures that the make_excel function is called only when the script is executed directly
if __name__ == "__main__":
    # Call the make_excel function with the country code "GB" to process data for Great Britain
    make_excel("GB")