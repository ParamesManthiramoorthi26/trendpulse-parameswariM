# TrendPulse Project – Grading Rubrics & Self-Check

This document outlines the grading criteria for each task in the TrendPulse project and provides a self-check list to ensure all requirements are met before submission.

---

## Task 1 – Data Collection

**Objective:** Collect Hacker News posts using the API and save them as JSON.

**Grading Criteria:**
- Script runs without errors
- Fetches at least 100 posts
- All required fields present: Post_id, title, author, score, num_comments, category, collected_at
- JSON saved in `data/` folder
- Code is clean and commented

---

## Task 2 – Data Processing

**Objective:** Load Task 1 JSON, clean the data, and save as CSV.

**Grading Criteria:**
- Script runs without errors
- JSON loaded correctly
- Missing values handled, duplicates removed
- Columns standardized (`category`, `title`, `author`)
- CSV saved in `data/` folder
- Code is clean and readable

---

## Task 3 – Data Analysis

**Objective:** Analyze cleaned data using Pandas & NumPy, add new analytical columns, save CSV.

**Grading Criteria:**
- Script runs without errors
- New columns added (e.g., `score_per_comment`)
- Category-level analysis (count, total score, total comments)
- Post-level analysis (highest score, most comments, highest/lowest score per comment)
- Author-level analysis (most posts, highest average score)
- CSV saved in `data/` folder
- Code is clean and readable

---

## Task 4 – Data Visualization & Dashboard

**Objective:** Create charts and a dashboard PNG for visual insights.

**Grading Criteria:**
- Script runs without errors
- Charts created: top posts, posts per category, scatter plot
- Dashboard created with 4 KPIs + 4 charts
- Titles, labels, legends, borders added
- Charts and dashboard saved in `outputs/` folder
- Code is clean and readable

---

## ✅ Self-Check Before Submission

Use this section to ensure all tasks are complete and meet the grading criteria.

### Task 1 – Data Collection
- [x] `task1_data_collection.py` runs without errors
- [x] JSON file saved in `data/` folder
- [x] At least 100 posts collected
- [x] Each post has all required fields
- [x] Code is commented and readable

### Task 2 – Data Processing
- [x] `task2_data_processing.py` runs without errors
- [x] JSON from Task 1 loaded correctly
- [x] Data cleaned: missing values handled, duplicates removed
- [x] Columns standardized
- [x] Output CSV saved in `data/` folder

### Task 3 – Data Analysis
- [x] `task3_analysis.py` runs without errors
- [x] New analytical columns added
- [x] Category-level analysis completed
- [x] Post-level analysis completed
- [x] Author-level analysis completed
- [x] Output CSV saved in `data/` folder

### Task 4 – Data Visualization & Dashboard
- [x] `task4_visualization.py` runs without errors
- [x] Charts created: top posts, posts per category, scatter plot
- [x] Dashboard created with 4 KPIs and 4 charts
- [x] Charts and dashboard saved in `outputs/` folder
- [x] Titles, labels, legends, borders added

---

