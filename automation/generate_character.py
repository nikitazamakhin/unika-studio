import os
import fal_client

def main():
    # Prompt for a modern, viral-worthy male pop star
    # Using specific keywords for realism and style
    base_prompts = [
        "A hyper-realistic portrait of a 20-year-old male K-pop star with silver hair, wearing a high-fashion white futuristic streetwear jacket, singing passionately into a microphone, stage lighting, bokeh, 8k, highly detailed, trending on artstation",
        "A charismatic male influencer singer, candid shot in a recording studio, wearing headphones, casual stylish hoodie, tattoos on neck, moody lighting, cinematographic, 35mm film grain, 8k",
        "A futuristic cybergoth male pop star performing on stage, neon lasers, intricate cyberpunk outfit, metallic makeup, dynamic pose, energetic atmosphere, hyper-detailed, unreal engine 5 render"
    ]

    print("Generating character concepts...")
    
    for i, prompt in enumerate(base_prompts):
        print(f"\n--- Concept {i+1} ---")
        image_url = fal_client.generate_image(prompt, image_size="portrait_9_16") # Vertical for Reels
        
        if image_url:
            print(f"Result {i+1}: {image_url}")
        else:
            print(f"Failed to generate Concept {i+1}")

if __name__ == "__main__":
    main()
