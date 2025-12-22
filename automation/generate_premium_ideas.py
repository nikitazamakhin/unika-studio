import sys
import os
# Add user site-packages explicitly
sys.path.append(os.path.expanduser("~/Library/Python/3.8/lib/python/site-packages"))
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env")
    exit(1)

genai.configure(api_key=GOOGLE_API_KEY)

def generate_ideas():
    print("Asking Gemini Pro for Premium Video Ideas...")
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = """
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
    
    response = model.generate_content(prompt)
    print("\n" + response.text)
    
    # Save to file
    with open("premium_ideas_gemini.md", "w") as f:
        f.write("# Gemini Pro Premium Concepts\n\n" + response.text)

if __name__ == "__main__":
    generate_ideas()
