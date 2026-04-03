# TrendPulse Hacker News Scraper – Task 1

## Project Overview
This script collects the **top stories from Hacker News** using the official API. It fetches story details, assigns categories based on keywords, and saves the results in a JSON file for further analysis.

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

