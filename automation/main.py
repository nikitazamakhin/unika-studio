import os
import sys
from dotenv import load_dotenv

def main():
    load_dotenv()
    print("Unika Studio Automation Tools")
    print("-----------------------------")
    print("1. Generate Viral Reel (Placeholder)")
    print("2. Process Commercial Assets (Placeholder)")
    
    choice = input("Select tool: ")
    
    if choice == "1":
        print("Starting viral content generation pipeline...")
        # TODO: Implement viral generation
    elif choice == "2":
        print("Starting commercial asset processing...")
        # TODO: Implement commercial processing
    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()
