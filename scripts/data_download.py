from urllib.request import urlretrieve
import os

# Set the relative directory where the downloaded files will be stored
output_relative_dir = '../data/landing'

# Check if the output directory exists, if not, create it
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

# Define the years and months to be downloaded
YEARS = ['2022', '2023']  # Years of interest
MONTHS = { '2022': range(11, 13), '2023': range(1, 5)}  # Months to download for each year (Nov-Dec for 2022, Jan-Apr for 2023)
TYPES = ['yellow']  # Taxi types to download, in this case only 'yellow'

# Base URL for downloading the data
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/"

# Loop through each taxi type, year, and month to download the respective data
for type in TYPES:
    for year in YEARS:
        month_range = MONTHS[year]
        for month in month_range:
            month = str(month).zfill(2)  # Ensure the month is two digits (e.g., '01' for January)
            
            # Inform the user that the download for a specific month is starting
            print(f"Begin month {type} for {month} of {year}:")

            # Construct the download URL and the local file path
            url = f'{URL_TEMPLATE}{type}_tripdata_{year}-{month}.parquet'
            output_dir = f"{output_relative_dir}/{type}_{year}_{month}.parquet"