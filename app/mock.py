"""
external_api.py
"""
import requests

EXTERNAL_API_URL = "https://catfact.ninja"

def fetch_random_fact() -> dict or None:
    response = requests.get(f"{EXTERNAL_API_URL}/fact", timeout=10)
    if response.status_code == 200:
        return response.json()
    return None

def process_fact(data) -> str or None:
    if data:
        return data.get("fact")
    return None

def fetch_last_page() -> dict or None:
    response = requests.get(f"{EXTERNAL_API_URL}/facts", timeout=10)
    if response.status_code == 200:
        return response.json()
    return None

def process_last_page(data) -> int or None:
    if data:
        return {key: val for key, val in data.items() if key in ('last_page')}
    return None

"""
main.py
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/random_fact")
async def get_random_fact():
    data: dict = fetch_random_fact()
    if data:
        return {"random fact": process_fact(data)}
    return {"error": "Failed to fetch data from external API"}

@app.get("/last_page")
async def get_last_page():
    data: dict = fetch_last_page()
    if data:
        return process_last_page(data)
    return {"error": "Failed to fetch data from external API"}
