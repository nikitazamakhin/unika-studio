import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

# Configuration
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
    print(f"Generating: {filename}...")
    payload = {
        "prompt": prompt,
        "image_size": "portrait_16_9",
        "num_inference_steps": 30,
        "guidance_scale": 3.5
    }
    
    try:
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if "images" in data:
                image_url = data["images"][0]["url"]
                save_image(image_url, filename)
                return image_url
            elif "status_url" in data:
                status_url = data["status_url"]
                response_url = data["response_url"]
                print(f"Queued. Polling {status_url}...")
                while True:
                    time.sleep(1)
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        # Check if images are here
                        if "images" in status_data:
                            image_url = status_data["images"][0]["url"]
                            save_image(image_url, filename)
                            return image_url
                        else:
                            # Fetch from response_url
                            print("Fetching result from response_url...")
                            res_response = requests.get(response_url, headers=HEADERS)
                            res_data = res_response.json()
                            if "images" in res_data:
                                image_url = res_data["images"][0]["url"]
                                save_image(image_url, filename)
                                return image_url
                            else:
                                print("No images in response_url result:", res_data)
                                break
                                
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed with status: {status}")
                        break
            else:
                print("No image or status in response:", data)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

def main():
    print("Starting generation for Case 1: Neon Energy (Cyberpunk)")
    
    shots = [
        {
            "filename": "shot_01_can.jpg",
            "prompt": "Cinematic product shot of a sleek aluminium energy drink can labeled 'NEON', glowing neon blue liquid inside, condensation droplets, floating in a futuristic cyberpunk alleyway, bokeh neon lights, purple and teal color palette, highly detailed, photorealistic, commercial photography, 8k"
        },
        {
            "filename": "shot_02_drinker.jpg",
            "prompt": "Portrait of a cyberpunk girl with glowing blue eyes drinking from a neon energy drink can, futuristic streetwear, rain, neon reflections on face, cinematic lighting, shallow depth of field, 8k"
        },
        {
            "filename": "shot_03_city.jpg",
            "prompt": "Hyper-lapse style wide shot of a futuristic mega-city at night, flying cars, massive holographic advertisements for 'NEON ENERGY', rainy atmosphere, blade runner aesthetic, dynamic angle, 8k"
        },
        {
            "filename": "shot_04_splash.jpg",
            "prompt": "High speed photography of neon blue energy liquid splashing out of a can, sparking electricity and lightning effects, dark background, frozen motion, macro detail"
        }
    ]

    for shot in shots:
        generate_image(shot["prompt"], shot["filename"])
        time.sleep(1)

if __name__ == "__main__":
    main()
