import requests
from fastapi import FastAPI, Depends

app = FastAPI()

EXTERNAL_API_URL = "https://catfact.ninja/fact"

def fetch_data_from_api():
    response = requests.get("EXTERNAL_API_URL")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_data(data):
    new_data = {}
    for key, value in data.items():
        new_data[key.upper()] = value.upper()
    return new_data

def get_and_process_data():
    data: dict = fetch_data_from_api()
    if data:
        return process_data(data)
    else:
        return {"error": "Failed to fetch data from the external API"}
