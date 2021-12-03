from datetime import datetime
from meteostat import Point, Daily
from multiprocessing import cpu_count
import numpy as np

from joblib import Parallel, delayed
import pandas as pd

def get_bulk_data(row):
    location = Point(row.lat, row.lon)
    data = Daily(location, row.Date, row.Date).fetch()
    data["latitude"] = row.lat
    data["longitude"] = row.lon
    return data

if __name__ == "__main__":
    df = pd.read_csv(r'C:\Users\leoac\OneDrive\Desktop\Coding\Python apps\Correlation temp-goals in Serie A\seasons 09-19.csv', sep=";", index_col= "indexes")
    df["Date"] = pd.to_datetime(df["Date"], format="%Y,%m,%d")

    executor = Parallel(n_jobs=cpu_count(), backend='multiprocessing')
    tasks = (
        delayed(get_bulk_data)(row)
        for _, row in df.iterrows()
    )
    list_of_locations_data = executor(tasks)
    data_full = pd.concat(list_of_locations_data)
    pd.DataFrame.to_csv(data_full,r"C:\Users\leoac\OneDrive\Desktop\Coding\Python apps\Correlation temp-goals in Serie A\data full aggiornati",";",columns=['tavg',"latitude","longitude"])

    print(data_full)