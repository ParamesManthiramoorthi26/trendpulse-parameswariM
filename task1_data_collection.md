# Task 1: Hacker News Trending Stories Collection

## Objective
The goal of Task 1 is to fetch the top 500 Hacker News stories, categorize them into predefined categories, and save a maximum of 25 stories per category into a JSON file for further analysis. The script ensures safe handling of network errors, SSL issues, and missing data.

## Features
- Fetches the top 500 Hacker News story IDs.
- Retrieves details for each story: **ID, title, author, score, number of comments**.
- Assigns categories using predefined keywords:

  | Category       | Keywords |
  | -------------- | -------- |
  | Technology     | AI, software, tech, code, computer, data, cloud, API, GPU, LLM |
  | Worldnews      | war, government, country, president, election, climate, attack, global |
  | Sports         | NFL, NBA, FIFA, sport, game, team, player, league, championship |
  | Science        | research, study, space, physics, biology, discovery, NASA, genome |
  | Entertainment  | movie, film, music, Netflix, game, book, show, award, streaming |

- Limits **up to 25 stories per category** to balance the dataset.
- Adds a **collected_at** timestamp for each story.
- Handles SSL errors and retries without crashing.
- Saves the collected stories as a **JSON file** in a `data/` folder.

---

## Required Fields for Each Post
Each story in the JSON file contains the following **7 fields**:

1. `Post_id` – Unique Hacker News story ID  
2. `title` – Story title  
3. `author` – Story author (`by` field)  
4. `score` – Story score (points)  
5. `num_comments` – Number of comments (`descendants`)  
6. `category` – Assigned category based on title  
7. `collected_at` – Timestamp when the story was collected  

---

### Run the script:

```bash
python task1_hackernews.py


The output JSON file will be saved in the data/ folder with the format:

data/trends_YYYYMMDD.json



Submission Checklist

- [x] Script runs without errors.
- [x] JSON file is saved in the data/ folder.
- [x] At least 100 posts are collected.
- [x] Each post has all 7 required fields:
- [x] Post_id, title, author, score, num_comments, category, collected_at.
- [x] Code is properly commented for clarity.


## Script Output

**Number of story IDs fetched:** 500  
**JSON file created:** `data/trends_20260404.json`  
**Total posts collected:** 113  

### Posts per Category

| Category       | Number of Posts |
|----------------|----------------|
| Technology     | 25             |
| World News     | 25             |
| Sports         | 2              |
| Science        | 11             |
| Entertainment  | 25             |
| Other          | 25             |