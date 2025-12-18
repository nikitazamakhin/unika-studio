import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

def test_fal_requests():
    print("Testing Fal.ai via HTTP Requests...")
    key = os.getenv("FAL_KEY")
    if not key:
        print("Error: FAL_KEY not found in .env")
        return

    url = "https://queue.fal.run/fal-ai/flux/schnell"
    headers = {
        "Authorization": f"Key {key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": "A cinematic shot of a futuristic neon city, cyberpunk style, golden hour, highly detailed, 4k"
    }

    try:
        print("Sending request...")
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return

        data = response.json()
        print("Request queued/processed. Checking status...")
        
        # Depending on if it's sync or async queue. fal.run usually returns 200 with result if fast, or queue info.
        # Flux Schnell is usually fast.
        
        if "images" in data:
            print("Generation successful!")
            print("Image URL:", data["images"][0]["url"])
        else:
            print("Response received (Async?):", data)

    except Exception as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":
    test_fal_requests()
