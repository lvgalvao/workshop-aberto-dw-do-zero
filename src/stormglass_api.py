import requests
from dotenv import load_dotenv
import os


load_dotenv()

STORMGLASS_API_KEY = os.getenv('STORMGLASS_API_KEY')

BASE_URL = 'https://api.stormglass.io/v2'

def get_wave_data(lat, lng):
    url = f'{BASE_URL}/weather/point'
    params = {
        'lat': lat,
        'lng': lng,
        'params': 'waveHeight,airTemperature,windSpeed',
        'source': 'noaa'
    }
    headers = {
        'Authorization': STORMGLASS_API_KEY
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data
