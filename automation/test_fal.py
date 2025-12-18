import os
import fal_client
from dotenv import load_dotenv

load_dotenv()

def test_fal():
    print("Testing Fal.ai connection...")
    key = os.getenv("FAL_KEY")
    if not key:
        print("Error: FAL_KEY not found in .env")
        return

    print(f"Key found: {key[:5]}...{key[-5:]}")
    
    try:
        # Simple test using a fast model (Flux Schnell)
        handler = fal_client.submit(
            "fal-ai/flux/schnell",
            arguments={
                "prompt": "A cinematic shot of a futuristic neon city, cyberpunk style, golden hour, highly detailed, 4k"
            },
        )
        
        print("Request submit success. Waiting for result...")
        result = handler.get()
        
        print("Generation successful!")
        print("Image URL:", result["images"][0]["url"])
        
    except Exception as e:
        print(f"Error during generation: {e}")

if __name__ == "__main__":
    test_fal()
