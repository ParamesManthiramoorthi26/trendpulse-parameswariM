#--------------Task 1 data collection -----------------
# Import required modules
import requests
import json
from datetime import datetime
import time
import os

# -----------------------------
# Define API URL
STORIESURL = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Fetch top 500 story IDs
response = requests.get(STORIESURL, headers={"User-Agent": "TrendPulse/1.0"})
if response.status_code == 200:
    storyids = response.json()[:500]
    print("Number of story IDs fetched:", len(storyids))
else:
    print("Error occurred:", response.status_code)
    storyids = []

# -----------------------------
# Expanded category keywords
CATEGORY_KEYWORDS = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "un", "politics"],
    "sports": [
    "nfl", "nba", "fifa", "sport", "team", "player", "league", "championship", 
    "cricket", "soccer", "tennis", "olympics", "football", "hockey", "baseball", 
    "rugby", "golf", "formula 1", "f1", "wimbledon", "world cup", "super bowl", 
    "champions league", "nba finals", "ncaa", "mlb", "soccer world cup"
],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome", "chemistry"],
    "entertainment": ["movie", "film", "music", "netflix", "book", "show", "award", "streaming", "concert", "series"]
}

# -----------------------------
# Function to assign category safely
def assign_category(title):
    if not title:  # handle empty or None title
        return "Other"
    title = title.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in title for word in keywords):
            return category
    return "Other"

# -----------------------------
# Initialize category counters
category_counts = {cat: 0 for cat in list(CATEGORY_KEYWORDS.keys()) + ["Other"]}
max_per_category = 25
all_story = []

# -----------------------------
# Function to fetch story with retry
def fetch_story(story_id, retries=1):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    headers = {"User-Agent": "TrendPulse/1.0"}
    for attempt in range(retries + 1):
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                return res.json()
        except requests.exceptions.RequestException as e:
            print(f"Error for ID {story_id}: {e}, retrying...")
            time.sleep(1)
    return None


# -----------------------------
# Main loop to fetch stories
for id in storyids:
    story = fetch_story(id, retries=1)
    if not story or story.get("type") != "story":
        continue


    title = story.get("title", "")
    category = assign_category(title)

    # Safety check
    if category not in category_counts:
        category = "Other"

    # Add story if category is not full
    if category_counts.get(category, 0) < max_per_category:
        story_data = {
            "Post_id": story.get("id"),
            "title": title,
            "author": story.get("by", "unknown"),
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "category": category,
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        all_story.append(story_data)
        category_counts[category] += 1

    # Stop if all categories reached max
    if all(count >= max_per_category for count in category_counts.values()):
        break

    time.sleep(0.2)  # gentle delay

# -----------------------------
# Make sure 'data/' folder exists
os.makedirs("data", exist_ok=True)

# Save to JSON with current date
today_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{today_str}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(all_story, f, ensure_ascii=False, indent=2)

# -----------------------------
# Print summary
print(f"{filename} created successfully")
print(f"Total posts collected: {len(all_story)}")
print("Posts per category:", category_counts)
