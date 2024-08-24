import streamlit as st
import json
import requests
#turn json format into tree
from pprint import pprint

st.title('My simple Weather App')

api_key = 'eb83b4c40cb20e8f56ad08567dcaadb7'  # replace with your actual API key


city = st.text_input('Enter a city: ')

if st.button('Get Weather'):
    #base url for query
    base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city+"&units=metric"
    #load as json file
    weather_data = requests.get(base_url).json()

    st.write(weather_data)

    if weather_data["cod"] != "404":  # check if the city is found
        main = weather_data["main"]
        temperature = main["temp"]
        # pressure = main["pressure"]
        humidity = main["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        country = weather_data["sys"]["country"]

        st.subheader(f"Weather in {city}, {country}:")

        st.write(f"It feels like {temperature}°C")
        # st.write(f"Atmospheric Pressure: {pressure} hPa")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Weather Description: {weather_desc}")
        st.write(f"Wind Speed: {wind_speed} m/s")

    else:
        st.write("City Not Found")
