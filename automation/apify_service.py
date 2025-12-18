
import os
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

class ApifyService:
    def __init__(self):
        self.api_token = os.getenv("APIFY_API_TOKEN")
        if not self.api_token:
            raise ValueError("APIFY_API_TOKEN is not set in .env")
        self.client = ApifyClient(self.api_token)

    def scrape_instagram_hashtag(self, hashtags: list, limit: int = 20):
        """
        Scrape Instagram posts/reels for specific hashtags.
        Uses the 'apify/instagram-hashtag-scraper' actor.
        """
        # Prepare the Actor input
        run_input = {
            "hashtags": hashtags,
            "resultsLimit": limit,
            "searchType": "hashtag",
            "searchLimit": 1, 
        }

        print(f"Starting Instagram scrape for hashtags: {hashtags} with limit {limit}...")
        
        # Run the Actor and wait for it to finish
        # Actor ID for Instagram Hashtag Scraper: apify/instagram-hashtag-scraper
        print("Calling Apify actor...")
        run = self.client.actor("apify/instagram-hashtag-scraper").call(run_input=run_input)
        
        print(f"Run finished with status: {run.get('status')}")
        print(f"Dataset ID: {run.get('defaultDatasetId')}")

        # Fetch and return Actor results from the run's dataset (if any)
        results = []
        dataset_items = self.client.dataset(run["defaultDatasetId"]).iterate_items()
        for item in dataset_items:
            results.append(item)
            
        print(f"Fetched {len(results)} items from dataset.")
        return results

    def scrape_trends(self):
        # Implementation for general trends if needed
        pass
