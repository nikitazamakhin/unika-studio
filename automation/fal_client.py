import os
import json
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()

FAL_KEY = os.getenv("FAL_KEY")

def generate_image(prompt, model="fal-ai/flux/schnell", image_size="landscape_4_3"):
    """
    Generates an image using Fal.ai via curl (to avoid python SSL issues).
    """
    if not FAL_KEY:
        print("Error: FAL_KEY not found")
        return None

    url = f"https://queue.fal.run/{model}"
    
    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": 4,
        "enable_safety_checker": False
    }

    print(f"Generating image with prompt: {prompt[:50]}...")
    
    try:
        # Construct curl command
        curl_cmd = [
            "curl", "-s", "-X", "POST", url,
            "-H", f"Authorization: Key {FAL_KEY}",
            "-H", "Content-Type: application/json",
            "-d", json.dumps(payload)
        ]
        
        result = subprocess.run(curl_cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Curl error: {result.stderr}")
            return None
            
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            print(f"Failed to decode JSON: {result.stdout}")
            return None
            
        if "images" in data:
            return data["images"][0]["url"]
        
        # Poll if needed
        if "request_id" in data:
            if "status_url" in data:
                return _poll_result(data["status_url"])
            # Fallback if status_url is missing (unlikely now)
            return None
            
        print(f"Unexpected response: {data}")
        return None

    except Exception as e:
        print(f"Error during generation: {e}")
        return None

def _poll_result(status_url):
    print(f"Polling {status_url}...")
    
    for _ in range(120):
        curl_cmd = [
            "curl", "-s", status_url,
            "-H", f"Authorization: Key {FAL_KEY}",
            "-H", "Content-Type: application/json"
        ]
        result = subprocess.run(curl_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                if "images" in data:
                    return data["images"][0]["url"]
                
                status = data.get("status")
                if status == "COMPLETED":
                    # Fetch from response_url
                    if "response_url" in data:
                        resp_url = data["response_url"]
                        print(f"Fetching result from {resp_url}...")
                        curl_cmd_res = [
                            "curl", "-s", resp_url,
                            "-H", f"Authorization: Key {FAL_KEY}",
                            "-H", "Content-Type: application/json"
                        ]
                        res_result = subprocess.run(curl_cmd_res, capture_output=True, text=True)
                        if res_result.returncode == 0:
                            res_data = json.loads(res_result.stdout)
                            if "images" in res_data:
                                return res_data["images"][0]["url"]
                
                if status in ["IN_QUEUE", "IN_PROGRESS"]:
                    time.sleep(1)
                    continue
            except:
                pass
        time.sleep(1)
    
    print("Timed out.")
    return None
