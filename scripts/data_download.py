from urllib.request import urlretrieve
import os

output_relative_dir = '../data/landing'

if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

YEARS = ['2022', '2023']
MONTHS = { '2022': range(11, 13), '2023': range(1, 5)}
TYPES = ['yellow']
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/"

for type in TYPES:
    for year in YEARS:
        month_range = MONTHS[year]
        for month in month_range:
            month = str(month).zfill(2)
            print(f"Begin month {type} for {month} of {year}:")
            url = f'{URL_TEMPLATE}{type}_tripdata_{year}-{month}.parquet'
            output_dir = f"{output_relative_dir}/{type}_{year}_{month}.parquet"
            urlretrieve(url, output_dir)
            print(f"Completed month {type} for {month} of {year}.")