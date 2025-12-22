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
    print(f"Animating Premium Shot: {image_filename}...")
    if not os.path.exists(image_filename):
        print(f"Error: {image_filename} not found!")
        return

    image_url = encode_image_to_base64_url(image_filename)
    
    payload = {
        "prompt": prompt,
        "image_url": image_url,
        "duration": duration,
        "aspect_ratio": "16:9",
        "camera_control": {
            "type": "zoom_out", # subtle zoom out for reveal
            "horizontal": 0,
            "vertical": 0,
            "zoom": 0.5 
        },
        "negative_prompt": "low quality, text distortion, warping, morphing logo, ugly, blurry"
    }
    
    try:
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if "status_url" in data:
                status_url = data["status_url"]
                response_url = data.get("response_url")
                print(f"Queued. Polling {status_url}...")
                while True:
                    time.sleep(5)
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        # Sometimes response_url is in status_data, sometimes we need to fetch the original response_url
                        # Kling via Fal usually returns result in status_data or response_url
                        
                        # Check status_data first
                        if "video" in status_data:
                             save_video(status_data["video"]["url"], output_filename)
                             break
                        
                        if response_url:
                            res_response = requests.get(response_url, headers=HEADERS)
                            res_data = res_response.json()
                            if "video" in res_data:
                                save_video(res_data["video"]["url"], output_filename)
                            elif "video_url" in res_data:
                                save_video(res_data["video_url"], output_filename)
                            else: 
                                print("No video in response:", res_data)
                        break
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed with status: {status}")
                        break
    except Exception as e:
        print(f"Exception: {e}")

def main():
    # Prompt emphasizing SLOW MOTION and PHYSICS
    prompt = (
        "Super slow motion 1000fps, extreme close-up product shot. "
        "The neon blue energy drink can stays perfectly still and stable. "
        "Crystal clear water splashes violently around it in zero gravity. "
        "Millions of tiny droplets suspended in the air. "
        "High speed phantom flex camera, cinematic lighting, sharp focus, 8k, liquid simulation C4D"
    )
    
    generate_video(
        "premium_poc_splash.jpg",
        prompt,
        "premium_splash_video.mp4"
    )

if __name__ == "__main__":
    main()
