#--------------Task 1 data collection -----------------
# Import required modules
import requests
import json
from datetime import datetime
import time
import os
import pandas as pd

#  Define the API URLs
STORIESURL = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(STORIESURL ,headers= {"User-Agent": "TrendPulse/1.0" })
if response.status_code == 200:
  # Fetch top 500 storyids
  storyids = response.json()[:500]
  print("Number of story IDs fetched:", len(storyids))
else :
  print("Error occurred:", response.status_code)

def assign_category(title):
    title = title.lower()
    if any(word in title for word in ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"]):
        return "technology"
    elif any(word in title for word in ["war", "government", "country", "president", "election", "climate", "attack", "global"]):
        return "worldnews"
    elif any(word in title for word in ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"]):
        return "sports"
    elif any(word in title for word in ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"]):
        return "science"
    elif any(word in title for word in ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]):
        return "entertainment"
    else:
        return "Other"

category_counts = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0,
    "Other": 0
}

max_per_category = 25
all_story = []
for id in storyids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    try:
        res = requests.get(url, headers={"User-Agent": "TrendPulse/1.0"}, timeout=10)
        story = res.json()
        if story and story.get("type") == "story":
            title = story.get("title", "")
            category = assign_category(title)

            # ✅ check limit BEFORE adding
            if category_counts.get(category, 0) < max_per_category:
                story_data = {
                    "Post_id": story.get("id"),
                    "title": title,
                    "author": story.get("by"),
                    "score": story.get("score"),
                    "num_comments": story.get("descendants"),
                    "category": category,
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                all_story.append(story_data)
                category_counts[category] += 1

        # ✅ stop when total reaches 125
        if sum(category_counts.values()) == 125:
            break

    except requests.exceptions.SSLError:
        print(f"SSL Error for ID {id}, retrying...")
        time.sleep(1)  # short delay
        try:
            res = requests.get(url, headers={"User-Agent": "TrendPulse/1.0"}, timeout=10)
            story = res.json()
            print(story)
        except:
            print(f"Failed again for ID {id}")
    time.sleep(0.2)  # gentle delay between requests


# Make sure 'data/' folder exists
os.makedirs("data", exist_ok=True)

# Get current date for filename
today_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{today_str}.json"

# Convert DataFrame to list of dictionaries
posts_list = df.to_dict(orient="records")

# Convert list of story dictionaries to JSON
with open(filename, "w", encoding="utf-8") as f:
    json.dump(all_story, f, ensure_ascii=False, indent=2)

# Print total posts collected
print(f"{filename} created successfully")
print(f"Total posts collected: {len(posts_list)}")

