import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

# Configuration
FAL_KEY = os.getenv("FAL_KEY")
# Using Kling Standard Image-to-Video
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

def generate_video(image_url, prompt, filename):
    print(f"Animating {filename} from {image_url}...")
    payload = {
        "prompt": prompt,
        "image_url": image_url,
        "duration": "5", # 5 or 10 seconds
        "aspect_ratio": "16:9" # matching the image_size portrait_16_9 roughly? Kling usually takes ratio.
        # Actually Kling might just take the image's ratio or have specific args.
        # Let's try standard payload.
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
                    time.sleep(2)
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        # Check for video in 'video' or 'video_url' or 'images' (some endpoints return video in images list lol)
                        
                        # Kling usually returns 'video' object or 'video_url'
                        print("Completed. Fetching result...")
                        # Best to fetch response_url to be safe as status might be partial
                        res_response = requests.get(response_url, headers=HEADERS)
                        res_data = res_response.json()
                        
                        if "video" in res_data:
                            video_url = res_data["video"]["url"]
                            save_video(video_url, filename)
                            return video_url
                        elif "video_url" in res_data:
                             save_video(res_data["video_url"], filename)
                             return res_data["video_url"]
                        else:
                            print("No video found in response:", res_data)
                            break
                                
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed with status: {status}")
                        print(status_data)
                        break
            else:
                print("No status_url in response:", data)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

# We need to upload the local image to a URL first if we want to use it, OR use the URL we got from generation if we persisted it.
# But typical Fal usage allows uploading file to fal storage.
# For now, I'll use the URL printed in previous step if I can recall it or I'll implementation a simple uploader.
# ACTUALLY, I don't have the URL persisted in a file. I only have the local file.
# I need to upload `shot_01_can.jpg`.
# Simpler: Fal has an upload endpoint `https://fal.media/upload` (usually via client).
# Since I am using raw requests, I'll implement a simple file upload to `https://fal.media/files/temp` or similar if documented.
# BETTER: I'll use `fal-ai/flux` output URL if I had saved it. I didn't save it to file, only printed.
# I can parse the logs of previous command?
# "Success! URL: https://v3b.fal.media/files/b/0a868f01/FbNYg-Sqh5qigYYS3i6DD.jpg"
# I can hardcode this URL for now to test.

def main():
    # Hardcoded URL from previous run for "shot_01_can.jpg"
    image_url = "https://v3b.fal.media/files/b/0a868f01/FbNYg-Sqh5qigYYS3i6DD.jpg" 
    
    prompt = "The can is floating and spinning slowly, electrical sparks and lightning surround it, liquid moving inside, cinematic, 8k"
    filename = "shot_01_video.mp4"
    
    generate_video(image_url, prompt, filename)

if __name__ == "__main__":
    main()
