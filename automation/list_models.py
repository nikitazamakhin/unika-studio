import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def list_models():
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GOOGLE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json().get('models', [])
        for m in models:
            if 'generateContent' in m['supportedGenerationMethods']:
                print(f"Name: {m['name']}")
    else:
        print(f"Error: {response.status_code} {response.text}")

if __name__ == "__main__":
    list_models()
