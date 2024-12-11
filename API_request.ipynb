# code to download Sparrow air measurments in Switzerland
# The API key you have determines which region and time period you have the measurements. 
# The measruemtns started around 2022, depending on the regions
# If you don't see measurements, it can mean the API doesn't have access to that region/period or Sparrow doesn't have that data
# As of Dec 2024, the API we have give us data for Lausanne and Berne
# Please don't share the API or the data! The API is only for URBES's usage.

import requests
import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point

# API endpoint
url = "https://api.sparrow.city/get/"

# Parameters for the GET request
params = {
    'filter': 'o3', # you can only choose one type of measurement like pm1,pm25,temperature at a time! other variables are in the document
    'start_date': '2024-07-15T00:00:00',
    'end_date': '2024-08-14T23:59:59',
    # paramters given by Sparrow for Lausanne. Adjust it for Berne if you like
    'start_lat': 46.5075, # 
    'start_lon': 6.5711, 
    'end_lat': 46.55, 
    'end_lon': 6.7081, 
    'api_key': 'the_API_key_I_sent_you'
}

# Headers for the GET request
headers = {
    'Accept-encoding': 'gzip'
}

# Sending the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parsing the JSON response
    print(data)  # Print or process the data as needed
else:
    print(f"Request failed with status code {response.status_code}")

# Assuming 'response' is the variable holding the response from the API
data = response.json()  # Convert the response to a JSON object
# Extract the 'body' part of the response, which contains the data records
records = data['body']

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(records)
df['t'] = pd.to_datetime(df.t, unit='s')
# Convert the DataFrame to a GeoDataFrame
df['geometry'] = df.apply(lambda row: Point(row['x'], row['y']), axis=1)
gdf = gpd.GeoDataFrame(df, geometry='geometry')
gdf.set_crs(epsg=4326, inplace=True)
print(len(gdf))
print(gdf.head(10))
# the measurments are in the 'v' column. For description of all the columns, see the document file
