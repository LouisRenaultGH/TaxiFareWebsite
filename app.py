import streamlit as st
import datetime
import requests

import pandas as pd
import numpy as np



@st.cache
def get_map_data():

    return pd.DataFrame(
            [[pu_lat, pu_long], [do_lat, do_long]],
            columns=['lat', 'lon']
        )
    
    
    
    
    
    

# pickup_date
pickup_date = st.date_input(
            "Date of pickup : ",
            datetime.datetime(2012, 10, 6))

t = st.time_input('Time of pickup', datetime.time(10, 20))

pickup_date = datetime.datetime(pickup_date.year, pickup_date.month, pickup_date.day, t.hour, t.minute)

# pickup_lag et long
pu_long = st.number_input('Pickup longitude', format='%.7f', value=40.7614327)
pu_lat = st.number_input('Pickup latitude', format='%.7f', value=-73.9798156)


# drop_offlag et long
do_long = st.number_input('Drop-off longitude', format='%.7f', value=40.6513111)
do_lat = st.number_input('Drop-off latitude', format='%.7f', value=-73.8803331)

# number of passengers
num_pass = st.number_input('Number of passengers', format='%d', step=1, min_value=0)


url = 'https://taxifare.lewagon.ai/predict'

if st.button('Predict'):
    # print is visible in the server output, not in the page    
    params = {"pickup_datetime":pickup_date,
          "pickup_longitude":pu_long,
          "pickup_latitude":pu_lat,
          "dropoff_longitude":do_long,
          "dropoff_latitude":do_lat,
          "passenger_count":num_pass}

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        st.success(f"Prediction : {response.json()['fare']} $")
        
        df = get_map_data()

        st.map(df)
        
    else:
        st.error(f"Une erreur est survenue : {response.status_code}")
    







