import os
import json
import subprocess
from dotenv import load_dotenv

load_dotenv()

FAL_KEY = os.getenv("FAL_KEY")

def debug_fal():
    url = "https://queue.fal.run/fal-ai/flux/schnell"
    payload = {
        "prompt": "A simple test circle",
        "image_size": "square_hd"
    }

    cmd = [
        "curl", "-s", "-X", "POST", url,
        "-H", f"Authorization: Key {FAL_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ]
    
    print("Sending POST request...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print("\n--- Response ---")
    print(result.stdout)

if __name__ == "__main__":
    debug_fal()
