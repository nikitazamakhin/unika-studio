import os
import requests
import json
import time
import base64
from dotenv import load_dotenv

load_dotenv()

FAL_KEY = os.getenv("FAL_KEY")
BASE_URL = "https://queue.fal.run/fal-ai/kling-video/v1/standard/image-to-video"
HEADERS = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}

def save_video(url, filename):
    print(f"Success! URL: {url}")
    try:
        vid_data = requests.get(url).content
        with open(filename, 'wb') as f:
            f.write(vid_data)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving video: {e}")

def encode_image_to_base64_url(image_filename):
    with open(image_filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_string}"

def generate_video(image_filename, prompt, output_filename, duration="5"):
    print(f"Animating {image_filename}...")
    image_url = encode_image_to_base64_url(image_filename)
    
    payload = {
        "prompt": prompt,
        "image_url": image_url,
        "duration": duration,
        "aspect_ratio": "16:9" 
    }
    
    try:
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if "status_url" in data:
                status_url = data["status_url"]
                response_url = data["response_url"]
                print(f"Queued. Polling {status_url}...")
                while True:
                    time.sleep(5)
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        res_response = requests.get(response_url, headers=HEADERS)
                        res_data = res_response.json()
                        if "video" in res_data:
                            save_video(res_data["video"]["url"], output_filename)
                        elif "video_url" in res_data:
                            save_video(res_data["video_url"], output_filename)
                        break
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed via poll. Status: {status}")
                        break
    except Exception as e:
        print(f"Exception: {e}")

def main():
    # 1. Renaissance -> Candle light, subtle divine movement
    generate_video(
        "lesson1_renaissance.jpg",
        "The energy drink glows with holy light, oil painting texture moving, dust particles, slow cinematic push in, dramatic lighting",
        "reel3_clip_01_renaissance.mp4"
    )
    
    # 2. Anime -> City lights moving, steam/smoke
    generate_video(
        "lesson1_anime.jpg",
        "Neon city lights reflecting on the can, rain falling, lo-fi anime aesthetic, steam rising from the can, loopable",
        "reel3_clip_02_anime.mp4"
    )
    
    # 3. Claymation -> Stop motion jitter
    generate_video(
        "lesson1_claymation.jpg",
        "Stop motion animation, the can wobbles slightly, plasticine texture changing, hand-made feel, cute movement",
        "reel3_clip_03_claymation.mp4"
    )

if __name__ == "__main__":
    main()
