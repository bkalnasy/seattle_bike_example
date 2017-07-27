import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename = "fremont.csv", url = FREMONT_URL, force_download = False):
    """" Download and cache the fremont data. Returns data as pandas.dataframe"""
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('fremont.csv', index_col ='Date')
    
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
        
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
