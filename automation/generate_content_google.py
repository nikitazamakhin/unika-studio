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
        print(f"💾 Saved to {filename}")
        return filename
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return None

def submit_request(endpoint, payload):
    url = f"https://queue.fal.run/{endpoint}"
    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def check_status(status_url):
    print(f"Polling status at: {status_url}")
    while True:
        response = requests.get(status_url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        
        status = data.get("status")
        if status == "COMPLETED":
            return requests.get(data["response_url"], headers=HEADERS).json()
        elif status == "FAILED":
            raise Exception(f"Generation failed: {data.get('error')}")
        
        print(f"⏳ Status: {status}...")
        time.sleep(1)

def main():
    print("🚀 Starting AI Pipeline with Google NanoBanano Pro...")
    
    if not FAL_KEY:
        print("❌ Error: FAL_KEY not set in .env")
        return

    # 1. Generate Image (Google Imagen 3)
    prompt = "A cinematic medium shot of a stunning cyberpunk girl with neon tattoos, standing in rain, wet skin texture, highly detailed face, 8k, photorealistic, masterpiece"
    print(f"1️⃣ Generating Image with Google Imagen 3...\nPrompt: {prompt}")
    
    try:
        # Submit to Google Imagen 3
        payload = {
            "prompt": prompt,
            "aspect_ratio": "9:16", # Imagen 3 uses aspect_ratio instead of image_size enum
            "safety_filter_level": "block_only_high" # Try to be permissive
        }
        submit_data = submit_request("fal-ai/imagen3", payload)
        status_url = submit_data["status_url"]
        
        # Poll
        result = check_status(status_url)
        
        # Nano Banana output structure matches standard Fal (usually)
        # But let's handle potential differences
        if "images" in result:
             image_url = result["images"][0]["url"]
        else:
             print("DEBUG: Result keys:", result.keys())
             image_url = result.get("image", {}).get("url") or result.get("url")
             
        if not image_url:
            raise Exception("Could not find image URL in response")
            
        print(f"✅ Image Generated (Google): {image_url}")
        local_image_path = save_file(image_url, "generated_image_google.jpg")
        if not local_image_path: return

        # 2. Animate (SVD)
        print("\n2️⃣ Animating Image with SVD...")
        
        svd_payload = {
            "image_url": image_url,
            "motion_bucket_id": 127,
            "cond_aug": 0.02
        }
        
        submit_data = submit_request("fal-ai/fast-svd", svd_payload)
        status_url = submit_data["status_url"]
        
        result = check_status(status_url)
        video_url = result["video"]["url"]
        print(f"✅ Video Generated: {video_url}")
        
        save_file(video_url, "generated_video_google.mp4")
        print("\n🎉 Pipeline Complete! Check 'generated_video_google.mp4'")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
