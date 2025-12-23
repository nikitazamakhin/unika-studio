import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

FAL_KEY = os.getenv("FAL_KEY")

def generate_image(prompt, model="fal-ai/flux/schnell", image_size="landscape_4_3"):
    """
    Generates an image using Fal.ai (Flux Schnell by default).
    """
    if not FAL_KEY:
        raise ValueError("FAL_KEY not found in environment variables")

    url = f"https://queue.fal.run/{model}"
    headers = {
        "Authorization": f"Key {FAL_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": 4, # Schnell is fast with fewer steps
        "enable_safety_checker": False
    }

    print(f"Generating image with prompt: {prompt[:50]}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        # For queue-based endpoints, we might need to poll, 
        # but Flux Schnell on fal.run is often synchronous-like or returns result quickly if using 'queue'??
        # Actually 'queue.fal.run' is the queue endpoint. 
        # Let's check if we strictly need to poll request_id.
        
        data = response.json()
        
        # If it returns a requestId, we might need to poll.
        if "request_id" in data and "images" not in data:
            request_id = data["request_id"]
            return _poll_result(url, request_id, headers)
        
        return data.get("images", [])[0].get("url")

    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def _poll_result(base_url, request_id, headers):
    status_url = f"{base_url}/requests/{request_id}"
    print(f"Polling for result {request_id}...")
    
    for _ in range(30): # Wait up to 30 seconds
        response = requests.get(status_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if "images" in data:
                return data["images"][0]["url"]
            if data.get("status") == "IN_QUEUE" or data.get("status") == "IN_PROGRESS":
                time.sleep(1)
                continue
        time.sleep(1)
    
    print("Timed out waiting for result.")
    return None
