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
    print(f"Generating Premium Styleframe: {filename}...")
    payload = {
        "prompt": prompt,
        "image_size": "portrait_16_9",
        "num_inference_steps": 40,
        "guidance_scale": 3.5, 
        "output_format": "jpeg"
    }
    
    try:
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if "images" in data:
                save_image(data["images"][0]["url"], filename)
            elif "status_url" in data:
                status_url = data["status_url"]
                print(f"Queued. Polling {status_url}...")
                while True:
                    time.sleep(2)
                    status_res = requests.get(status_url, headers=HEADERS)
                    status_data = status_res.json()
                    status = status_data.get("status")
                    
                    if status == "COMPLETED":
                        if "images" in status_data:
                            save_image(status_data["images"][0]["url"], filename)
                        break
                    elif status == "IN_QUEUE" or status == "IN_PROGRESS":
                        continue
                    else:
                        print(f"Failed with status: {status}")
                        break
    except Exception as e:
        print(f"Exception: {e}")

def main():
    concepts = [
        {
            "file": "concept_1_cryo_crown.jpg",
            "prompt": "Commercial macro photography of a neon blue liquid drop freezing into a sharp fractal crystal crown in mid-air. Intense electric blue glow, black background, 8k resolution, phase one camera, hyper-realistic ice texture."
        },
        {
            "file": "concept_2_hydro_singularity.jpg",
            "prompt": "Abstract commercial shot of neon blue liquid forming a perfect vertical geometric lattice wall on a vibrating black titanium disk. Chladni pattern, physics simulation, studio lighting, hyper-sharp focus."
        },
        {
            "file": "concept_3_subsurface.jpg",
            "prompt": "Underwater macro shot inside a thick neon blue liquid. Bright electric arc lightning traveling through the fluid. Micro-bubbles, volumetric lighting, depth of field, cinematic scientific visualization."
        },
        {
            "file": "concept_4_acoustic_dome.jpg",
            "prompt": "Extreme close-up of a perfect spherical dome of blue liquid rising from a flat surface due to sound vibration. Mercury-like reflection, studio lighting, frozen in time, high speed photography."
        },
        {
            "file": "concept_5_helix.jpg",
            "prompt": "Two streams of liquid (electric blue and white) colliding and twisting into a perfect double helix DNA structure. Dark background, glowing liquid, subsurface scattering, 3D render style, clean composition."
        }
    ]
    
    for c in concepts:
        generate_image(c["prompt"], c["file"])

if __name__ == "__main__":
    main()
