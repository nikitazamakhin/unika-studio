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

def generate_video_from_image_file(image_filename, prompt, output_filename):
    print(f"Animating {image_filename}...")
    
    # Encode as Data URI
    image_url = encode_image_to_base64_url(image_filename)
    # print(f"Encoded image size: {len(image_url)}")

    payload = {
        "prompt": prompt,
        "image_url": image_url,
        "duration": "5",
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
                    time.sleep(5) # Poll less frequently for video
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        # Fetch from response_url
                        res_response = requests.get(response_url, headers=HEADERS)
                        res_data = res_response.json()
                        
                        if "video" in res_data:
                            video_url = res_data["video"]["url"]
                            save_video(video_url, output_filename)
                            break
                        elif "video_url" in res_data:
                             save_video(res_data["video_url"], output_filename)
                             break
                        else:
                            print("No video found:", res_data)
                            break
                                
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed with status: {status}")
                        break
    except Exception as e:
        print(f"Exception: {e}")

def main():
    scenes = [
        {"img": "v2_shot_01_mountain.jpg", "vid": "v2_clip_01_mountain.mp4", "prompt": "The energy drink can is flying through the air with white wings flapping, snowy mountains in background, cinematic, 8k"},
        {"img": "v2_shot_02_ocean.jpg", "vid": "v2_clip_02_ocean.mp4", "prompt": "The can dives into the water, bubbles rising, underwater distortion, sun rays, cinematic lighting"},
        {"img": "v2_shot_03_safari.jpg", "vid": "v2_clip_03_safari.mp4", "prompt": "View from bus window, lions walking in background, dust motes dancing, can sitting on ledge, parallax movement"},
        {"img": "v2_shot_04_nyc.jpg", "vid": "v2_clip_04_nyc.mp4", "prompt": "Rain droplets moving on window, city lights passing by, hand holding the can slightly shaking, urban atmosphere"},
        {"img": "v2_shot_05_smoke.jpg", "vid": "v2_clip_05_smoke.mp4", "prompt": "Colorful smoke pouring out of the can, swirling, dramatic rim lighting, studio shot"}
    ]

    for scene in scenes:
        if os.path.exists(scene["img"]):
            if not os.path.exists(scene["vid"]):
                generate_video_from_image_file(scene["img"], scene["prompt"], scene["vid"])
            else:
                print(f"Skipping {scene['vid']} (exists)")
        else:
            print(f"Missing input image: {scene['img']}")

if __name__ == "__main__":
    main()
