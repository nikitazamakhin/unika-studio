import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

FAL_KEY = os.getenv("FAL_KEY")
BASE_URL = "https://queue.fal.run/fal-ai/flux/dev"
HEADERS = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}

def save_image(url, filename):
    print(f"Success! URL: {url}")
    try:
        img_data = requests.get(url).content
        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")

def generate_image(prompt, filename):
    print(f"Generating Premium POC: {filename}...")
    payload = {
        "prompt": prompt,
        "image_size": "portrait_16_9",
        "num_inference_steps": 40, # Higher steps for quality
        "guidance_scale": 3.0 # Slightly lower for more realism/less frying
    }
    
    try:
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if "images" in data:
                image_url = data["images"][0]["url"]
                save_image(image_url, filename)
            elif "status_url" in data:
                status_url = data["status_url"]
                response_url = data.get("response_url")
                print(f"Queued. Polling {status_url}...")
                while True:
                    time.sleep(1)
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        if "images" in status_data:
                            image_url = status_data["images"][0]["url"]
                            save_image(image_url, filename)
                        elif response_url:
                            res_response = requests.get(response_url, headers=HEADERS)
                            res_data = res_response.json()
                            if "images" in res_data:
                                image_url = res_data["images"][0]["url"]
                                save_image(image_url, filename)
                        break
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed with status: {status}")
                        break
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

def main():
    print("Starting Premium POC Generation...")
    
    # "The Liquid Explosion"
    prompt = (
        "Professional commercial photography of a sleek neon blue energy drink can labeled 'NEON', "
        "violently splashing into crystal clear water, millions of tiny droplets frozen in mid-air, "
        "dramatic studio rime lighting, cold condensation on the metal, 8k resolution, "
        "phase one camera, hyper-realistic, unreal engine 5 render style, liquid simulation, "
        "centered composition"
    )
    
    generate_image(prompt, "premium_poc_splash.jpg")

if __name__ == "__main__":
    main()
