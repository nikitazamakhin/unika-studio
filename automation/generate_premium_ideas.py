import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env")
    exit(1)

def generate_ideas():
    print("Asking Gemini Pro for Premium Video Ideas (via REST API)...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={GOOGLE_API_KEY}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    prompt_text = """
    You are a world-class Clio Award winning commercial director.
    We are making a high-end CGI commercial for a neon-blue energy drink called "NEON".
    
    Generate 5 extremely expensive-looking, visually stunning video concepts (10 seconds each).
    Focus on: Liquid physics, Macro shots, Lighting, Slow Motion.
    
    Format each idea as:
    **[Title]**
    *   **Visual:** [Detailed description of the shot]
    *   **Camera:** [Camera movement]
    *   **Prompt Keyword:** [Key words for AI generation]
    """
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt_text}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            try:
                # Extract text from response structure
                generated_text = data["candidates"][0]["content"]["parts"][0]["text"]
                print("\n" + generated_text)
                
                # Save to file
                with open("premium_ideas_gemini.md", "w") as f:
                    f.write("# Gemini Pro Premium Concepts\n\n" + generated_text)
                print("\nSuccess! Saved to premium_ideas_gemini.md")
                
            except (KeyError, IndexError) as e:
                print(f"Error parsing response: {e}")
                print(data)
        else:
            print(f"Error {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    generate_ideas()
