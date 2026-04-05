# TrendPulse Project – Grading Rubrics & Self-Check

This document outlines the grading criteria for each task in the TrendPulse project and provides a self-check list to ensure all requirements are met before submission.

---

## Task 1 – Data Collection

**Objective:** Fetch top Hacker News posts using the API, categorize by keywords, and save as JSON.

**Grading Criteria:**
- Script runs without errors
- Fetches top 500 posts (or all available) and collects up to 25 per category
- Assigns category safely using keywords
- Handles failed requests and retries
- Adds `collected_at` timestamp
- JSON saved in `data/` folder
- Code is clean, readable, and commented

---

## Task 2 – Data Processing

**Objective:** Load Task 1 JSON, clean the data, handle missing values, standardize columns, and save as CSV.

**Grading Criteria:**
- Script runs without errors
- JSON loaded correctly
- Missing values handled and duplicates removed
- Columns standardized: `category`, `title`, `author`, `score`, `num_comments`
- Output CSV saved in `data/` folder
- Code is clean and readable

---

## Task 3 – Data Analysis

**Objective:** Analyze cleaned data using Pandas & NumPy, compute statistics, add new columns, and save for Task 4.

**Grading Criteria:**
- Script runs without errors
- Loads `data/trends_clean.csv` correctly
- Prints first 5 rows and shape of the DataFrame
- Prints average score and average num_comments
- Uses NumPy to calculate:
  - Mean, median, and standard deviation of `score`
  - Maximum and minimum `score`
  - Category with most stories
  - Story with most comments (title and comment count)
- Adds two new columns:
  - `Engagement = num_comments / (score + 1)` (discussion per upvote)
  - `Is_popular = True if score > average score, else False`
- Saves updated DataFrame to `data/trends_analysed.csv`
- Prints confirmation message after saving
- Code is commented, readable, and uses NumPy for calculations

---

## Task 4 – Data Visualization & Dashboard

**Objective:** Create visual insights from analyzed data, including individual charts and a combined dashboard.

**Grading Criteria:**
- Script runs without errors
- Charts created:
  - Top 10 stories by score (horizontal bar chart)
  - Stories per category (bar chart)
  - Score vs num_comments (scatter plot with popular vs non-popular coloring)
- Dashboard created:
  - Layout: top-left top story chart, top-right posts per category, bottom scatter plot
  - Overall title: "TrendPulse Dashboard"
  - Saved as `outputs/dashboard.png`
- Charts saved individually in `outputs/` folder:
  - `chart1_top_stories.png`
  - `chart2_categories.png`
  - `chart3_scatter.png`
- Titles, axis labels, legends, and borders added
- Code is clean and readable

---

## ✅ Self-Check Before Submission

Use this section to ensure all tasks are complete and meet the grading criteria.

### Task 1 – Data Collection
- [x] `task1_data_collection.py` runs without errors
- [x] JSON file saved in `data/` folder
- [x] Top posts collected (up to 25 per category)
- [x] Each post has all required fields: Post_id, title, author, score, num_comments, category, collected_at
- [x] Code is commented and readable

### Task 2 – Data Processing
- [x] `task2_data_processing.py` runs without errors
- [x] JSON from Task 1 loaded correctly
- [x] Data cleaned: missing values handled, duplicates removed
- [x] Columns standardized
- [x] Output CSV saved in `data/` folder

### Task 3 – Data Analysis
- [x] `task3_analysis.py` runs without errors
- [x] First 5 rows and DataFrame shape printed
- [x] Average score and average num_comments printed
- [x] NumPy used to calculate mean, median, std, max, min, most stories, most commented story
- [x] `Engagement` and `Is_popular` columns added correctly
- [x] `data/trends_analysed.csv` saved
- [x] Code is commented and readable

### Task 4 – Data Visualization & Dashboard
- [x] `task4_visualization.py` runs without errors
- [x] Individual charts created:
  - Top 10 stories by score
  - Posts per category
  - Score vs num_comments scatter plot
- [x] Dashboard created with top-left, top-right, and bottom chart layout
- [x] Charts and dashboard saved in `outputs/` folder
- [x] Titles, labels, legends, borders added
