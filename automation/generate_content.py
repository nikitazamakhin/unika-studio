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

def upload_file(path):
    # Get upload URL
    print(f"⬆️ Uploading {path}...")
    headers = {"Authorization": f"Key {FAL_KEY}"}
    
    # 1. Initiate upload
    init_url = "https://rest.alpha.fal.ai/storage/upload/initiate"
    init_resp = requests.post(
        init_url, 
        headers=headers, 
        data={"content_type": "image/jpeg", "file_name": os.path.basename(path)}
    )
    # Fallback if alpha endpoint changes or fails - actually fal-client handles this complex logic.
    # To keep it simple without SDK, we might struggle with direct upload.
    # ALTERNATIVE: Use a temporary public URL or just base64? 
    # Fal often accepts Base64 Data URIs. Let's try that.
    
    import base64
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_string}"

def main():
    print("🚀 Starting AI Content Pipeline (Requests Mode)...")
    
    if not FAL_KEY:
        print("❌ Error: FAL_KEY not set in .env")
        return

    # 1. Generate Image (Flux Dev)
    prompt = "A cinematic medium shot of a stunning cyberpunk girl with neon tattoos, standing in rain, wet skin texture, highly detailed face, 8k, photorealistic, masterpiece"
    print(f"1️⃣ Generating Image with Flux Dev...\nPrompt: {prompt}")
    
    try:
        # Submit
        payload = {
            "prompt": prompt,
            "image_size": "portrait_16_9",
            "num_inference_steps": 30,
            "guidance_scale": 3.5,
            "enable_safety_checker": False
        }
        submit_data = submit_request("fal-ai/flux/dev", payload)
        status_url = submit_data["status_url"]
        
        # Poll
        result = check_status(status_url)
        image_url = result["images"][0]["url"]
        print(f"✅ Image Generated: {image_url}")
        
        local_image_path = save_file(image_url, "generated_image.jpg")
        if not local_image_path: return

        # 2. Animate (SVD)
        print("\n2️⃣ Animating Image with SVD...")
        
        # For simplicity in 'requests' mode, we pass the image_url directly if it's public.
        # Fal generation URLs are usually temporary public URLs.
        
        svd_payload = {
            "image_url": image_url, # Using the URL directly from Flux output
            "motion_bucket_id": 127,
            "cond_aug": 0.02
        }
        
        submit_data = submit_request("fal-ai/fast-svd", svd_payload)
        status_url = submit_data["status_url"]
        
        result = check_status(status_url)
        video_url = result["video"]["url"]
        print(f"✅ Video Generated: {video_url}")
        
        save_file(video_url, "generated_video.mp4")
        print("\n🎉 Pipeline Complete! Check 'generated_video.mp4'")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
