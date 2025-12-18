import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

FAL_KEY = os.getenv("FAL_KEY")
HEADERS = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}

def save_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"💾 Saved {filename}")
        return filename
    except Exception as e:
        print(f"❌ Failed download {filename}: {e}")
        return None

def submit_request(endpoint, payload):
    url = f"https://queue.fal.run/{endpoint}"
    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def check_status(status_url):
    print(f"Polling: {status_url}")
    while True:
        response = requests.get(status_url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        status = data.get("status")
        
        if status == "COMPLETED":
            return requests.get(data["response_url"], headers=HEADERS).json()
        elif status == "FAILED":
            raise Exception(f"Failed: {data.get('error')}")
        
        print(f"⏳ Status: {status}...")
        time.sleep(2)

def main():
    print("🚀 Starting Kling 10s Action Pipeline...")
    
    # 1. Generate Source Image (Google Imagen 3)
    # We need a full body shot to allow for the dismounting action
    prompt = "Full body wide shot of a stunning cyberpunk girl with neon tattoos, sitting on a massive futuristic black motorcycle, rainy neon city street, wearing a long translucent skirt and leather jacket, highly detailed, 8k, masterpiece"
    print(f"1️⃣  Generating Base Image (Google Imagen 3)...\nPrompt: {prompt}")
    
    try:
        img_payload = {
            "prompt": prompt,
            "aspect_ratio": "9:16",
            "safety_filter_level": "block_only_high"
        }
        submit = submit_request("fal-ai/imagen3", img_payload)
        img_result = check_status(submit["status_url"])
        
        if "images" in img_result:
             img_url = img_result["images"][0]["url"]
        else:
             print("DEBUG Imagen Result:", img_result)
             img_url = img_result.get("image", {}).get("url") or img_result.get("url")
             
        if not img_url:
            raise Exception("Failed to extract image URL from Imagen response")

        print(f"✅ Base Image Ready: {img_url}")
        save_file(img_url, "kling_source.jpg")
        
        # 2. Animate with Kling (10s Action)
        print("\n2️⃣  Sending to Kling AI (10s Video)...")
        print("Prompt: Dismounting motorcycle, adjusting skirt...")
        
        kling_payload = {
            "image_url": img_url,
            "prompt": "The girl gracefully stands up and gets off the motorcycle, then she smooths and adjusts her long skirt, fashion pose, slow motion, cinematic lighting",
            "duration": "10", # 10 seconds
            "aspect_ratio": "9:16"
        }
        
        # Kling Image-to-Video endpoint (v1.6 Pro)
        submit_kling = submit_request("fal-ai/kling-video/v1.6/pro/image-to-video", kling_payload)
        vid_result = check_status(submit_kling["status_url"])
        
        if "video" in vid_result:
            vid_url = vid_result["video"]["url"]
            print(f"✅ Kling Video Ready: {vid_url}")
            save_file(vid_url, "kling_action_10s.mp4")
            print("\n🎉 Done! Check 'kling_action_10s.mp4'")
        else:
             print("DEBUG Result:", vid_result)
             
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
