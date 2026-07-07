import pandas as pd

import numpy as np

from six.moves import urllib

import os

import warnings

warnings.filterwarnings("ignore")
data_dir = "./data/"

os.makedirs(data_dir, exist_ok=True)

data_urls = ("https://raw.githubusercontent.com/mohitmahi004/atliq_hotels_data/refs/heads/main/dim_date.csv",

             "https://raw.githubusercontent.com/mohitmahi004/atliq_hotels_data/refs/heads/main/dim_hotels.csv",

             "https://raw.githubusercontent.com/mohitmahi004/atliq_hotels_data/refs/heads/main/dim_rooms.csv",

             "https://raw.githubusercontent.com/mohitmahi004/atliq_hotels_data/refs/heads/main/fact_aggregated_bookings.csv",

             "https://raw.githubusercontent.com/mohitmahi004/atliq_hotels_data/refs/heads/main/fact_bookings.csv")

for data_url in data_urls:

    print("__"*50)

    filename = os.path.basename(data_url)

    print(f"Downloading : {filename}")

    filepath = os.path.join(data_dir, filename)

    print(f"Saving at : {filepath}")

    urllib.request.urlretrieve(data_url,filepath)

    print("Downloading completed")
df_dim_date=pd.read_csv("./data/dim_date.csv")
df_dim_date
df_dim_date.info()
df_dim_date.isnull().sum()
df_dim_date['date'] = pd.to_datetime(df_dim_date["date"])
df_dim_date.dtypes

df_dim_hotels=pd.read_csv("./data/dim_hotels.csv")
df_dim_hotels
df_dim_hotels.info()
df_dim_hotels.isnull().sum()

df_dim_rooms=pd.read_csv("./data/dim_rooms.csv")
df_dim_rooms
df_dim_rooms.info()
df_dim_rooms.isnull().sum()

df_fact_aggregated_bookings=pd.read_csv("./data/fact_aggregated_bookings.csv")
df_fact_aggregated_bookings

df_fact_aggregated_bookings.info()
df_fact_aggregated_bookings['check_in_date'] = pd.to_datetime(df_fact_aggregated_bookings["check_in_date"])
df_fact_aggregated_bookings
df_fact_bookings=pd.read_csv("./data/fact_bookings.csv")
df_fact_bookings

df_fact_bookings.info()
df_fact_bookings['booking_date'] = pd.to_datetime(df_fact_bookings["booking_date"])
df_fact_bookings['check_in_date'] = pd.to_datetime(df_fact_bookings["check_in_date"])
df_fact_bookings['checkout_date'] = pd.to_datetime(df_fact_bookings["checkout_date"])
df_fact_bookings
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost:3306/{db}".format(user='root', pw='Pj00000', db='hotel_rev_insights_db'))
df_dim_date.to_sql(con=engine, name="dim_date", index=False, if_exists='replace')
df_dim_hotels.to_sql(con=engine, name="dim_hotels", index=False, if_exists='replace')
df_dim_rooms.to_sql(con=engine, name="dim_rooms", index=False, if_exists='replace')
df_fact_aggregated_bookings.to_sql(con=engine, name="fact_aggregated_bookings", index=False, if_exists='replace')
df_fact_bookings.to_sql(con=engine, name="fact_bookings", index=False, if_exists='replace')
