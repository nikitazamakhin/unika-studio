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
                        else:
                            print("No video found:", res_data)
                        break
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed via poll. Status: {status}")
                        break
    except Exception as e:
        print(f"Exception: {e}")

def main():
    # 1. Trash Room -> User splashing water/drink?
    # We want movement: "Hand pours drink, splash hits wall"
    generate_video(
        "trash_room.jpg",
        "POV shot, hand shakes the can violently and splashes neon blue liquid forward onto the peeling wall, fluid simulation, dynamic motion, chaotic, cinematic",
        "reel2_clip_01_splash.mp4"
    )
    
    # 2. Lion Room -> Lion moving
    generate_video(
        "lion_room.jpg",
        "The lion turns its head to look at the camera, wearing a crown, blinking, breathing, royal atmosphere, cinematic lighting, 8k",
        "reel2_clip_02_lion.mp4"
    )
    
    # 3. Luxury Room -> Just a nice pan or glitch?
    # Let's animate a glitch reveal or just a steady shot.
    generate_video(
        "luxury_room.jpg",
        "Camera pushes in slowly, golden light shimmers, sparkles in the air, highly detailed, smooth motion",
        "reel2_clip_03_luxury.mp4"
    )

if __name__ == "__main__":
    main()
