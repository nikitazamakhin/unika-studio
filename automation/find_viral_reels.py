
from apify_service import ApifyService
import sys

def main():
    service = ApifyService()
    
    # Hashtags to search for viral AI content
    hashtags = ["aivideo", "runwayml", "klingai", "lumadreammachine", "aifilm", "generativevideo"]
    
    try:
        results = service.scrape_instagram_hashtag(hashtags, limit=60)
        
        if not results:
            print("No results found.")
            return

        # Filter for content that is likely video or high engagement
        viral_candidates = []
        for item in results:
            # We accept Videos, Sidecars (often contain mixed media/video), or anything with a videoDuration
            is_potential_video = (
                item.get('type') in ['Video', 'Sidecar'] or 
                item.get('productType') in ['clips', 'carousel_container'] or
                item.get('videoDuration', 0) > 0
            )
            if is_potential_video:
                viral_candidates.append(item)
            
        print(f"\nFound {len(viral_candidates)} viral candidates. Sorting by likes...\n")
        
        # Sort by engagement (likesCount)
        viral_candidates.sort(key=lambda x: x.get('likesCount', 0), reverse=True)
        
        # If no candidates found (unlikely), fallback
        if not viral_candidates:
             viral_candidates = results
             viral_candidates.sort(key=lambda x: x.get('likesCount', 0), reverse=True)

        top_candidates = viral_candidates[:10]
        
        for row in top_candidates:
             # Basic info
             print(f"Type: {row.get('type')}")
             print(f"URL: {row.get('url')}")
             print(f"Likes: {row.get('likesCount')}")
             # Clean caption for display
             caption = (row.get('caption') or '').replace('\n', ' ')[:80]
             print(f"Caption: {caption}...")
             print("-" * 30)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
