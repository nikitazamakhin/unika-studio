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
            elif "status_url" in data: # Handle Async Queue
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
                            return image_url
                        elif response_url:
                             # Fetch from response_url
                            res_response = requests.get(response_url, headers=HEADERS)
                            res_data = res_response.json()
                            if "images" in res_data:
                                image_url = res_data["images"][0]["url"]
                                save_image(image_url, filename)
                                return image_url
                        
                        print("No images found in completed response")
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
    print("Starting generation for Reel 1 V2: Complex Journey")
    
    shots = [
        {
            "filename": "v2_shot_01_mountain.jpg",
            "prompt": "Cinematic shot of a sleek neon blue energy drink can with white feathery wings flying mid-air off a snowy mountain peak, dynamic motion, blue sky, photorealistic, 8k, surreal advertising"
        },
        {
            "filename": "v2_shot_02_ocean.jpg",
            "prompt": "Cinematic underwater shot of a neon energy drink can diving into deep blue ocean water, bubbles, sun rays piercing through the surface, high detail, 8k"
        },
        {
            "filename": "v2_shot_03_safari.jpg",
            "prompt": "Cinematic shot from inside a vintage safari bus window looking out, a neon energy drink can sitting on the window ledge, wild lions resting in the savannah background, dusty golden hour lighting, 8k"
        },
        {
            "filename": "v2_shot_04_nyc.jpg",
            "prompt": "POV shot holding a neon energy drink can inside a yellow taxi cab in New York City, rain droplets on window, blurred Times Square neon lights in background, urban atmosphere, 8k"
        },
        {
            "filename": "v2_shot_05_smoke.jpg",
            "prompt": "Studio product shot of a neon energy drink can centered, beautiful colorful pink and blue smoke conducting out of the opening, dramatic rim lighting, dark background, 8k, cinematic masterpiece"
        }
    ]

    for shot in shots:
        if not os.path.exists(shot["filename"]):
             generate_image(shot["prompt"], shot["filename"])
             time.sleep(1)
        else:
             print(f"Skipping {shot['filename']} (exists)")

if __name__ == "__main__":
    main()
