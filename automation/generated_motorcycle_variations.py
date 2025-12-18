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
    while True:
        response = requests.get(status_url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data["status"] == "COMPLETED":
            return requests.get(data["response_url"], headers=HEADERS).json()
        elif data["status"] == "FAILED":
            raise Exception(f"Failed: {data.get('error')}")
        time.sleep(1)

def main():
    print("🚀 Generating 3 Motorcycle Variations...")
    
    # Base prompt with "sitting on motorcycle" added
    base_prompt = "A cinematic medium shot of a stunning cyberpunk girl with neon tattoos, sitting on a futuristic black motorcycle, neon city background, rain, wet skin texture, highly detailed face, 8k, photorealistic, masterpiece"
    
    for i in range(1, 4):
        print(f"\n🎬 Scene {i}: Generating Image...")
        
        # 1. Generate Image (Google Imagen 3 for quality)
        try:
            payload = {
                "prompt": base_prompt + f", variation {i}", # Add variation noise to prompt
                "aspect_ratio": "9:16",
                "safety_filter_level": "block_only_high"
            }
            submit = submit_request("fal-ai/imagen3", payload)
            result = check_status(submit["status_url"])
            
            # Handle Google's sometimes varying response structure
            img_url = result.get("images", [{}])[0].get("url") or result.get("url")
            if not img_url: raise Exception("No image URL")
            
            print(f"✅ Image {i} Ready: {img_url}")
            save_file(img_url, f"moto_girl_{i}.jpg")
            
            # 2. Animate (SVD)
            print(f"⚡️ Animating Scene {i}...")
            svd_payload = {
                "image_url": img_url,
                "motion_bucket_id": 140, # More motion for motorcycle scene
                "cond_aug": 0.02
            }
            submit_svd = submit_request("fal-ai/fast-svd", svd_payload)
            vid_result = check_status(submit_svd["status_url"])
            vid_url = vid_result["video"]["url"]
            
            print(f"✅ Video {i} Ready: {vid_url}")
            save_file(vid_url, f"moto_video_{i}.mp4")
            
        except Exception as e:
            print(f"❌ Error in Scene {i}: {e}")

if __name__ == "__main__":
    main()
