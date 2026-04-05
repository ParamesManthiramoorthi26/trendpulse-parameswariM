# Task 2 — Clean the Data & Save as CSV
---

## Objective
The raw JSON data from Task 1 may have messy entries — duplicates, missing values, wrong data types, extra whitespace, or low-quality posts.  

The goal of Task 2 is to **load the JSON into a Pandas DataFrame, clean it, remove low-quality stories, and save it as a tidy CSV file** for further analysis.

---

## Input
- JSON file from Task 1:  
  `data/trends_YYYYMMDD.json`  
- Contains posts with fields:  
  `Post_id`, `title`, `author`, `score`, `num_comments`, `category`, `collected_at`.

---

## Tasks

### 1 — Load the JSON File (4 marks)
- Load the JSON into a Pandas DataFrame.  
- Print the number of rows and columns loaded.  
- Preview the first and last 5 rows.

### 2 — Clean the Data (10 marks)
Fix the following issues:
- **Duplicates:** Remove rows with the same `Post_id`.  
- **Missing values:** Drop rows where `Post_id`, `title`, or `score` is missing.  
- **Data types:** Ensure `score` and `num_comments` are integers.  
- **Low quality:** Remove stories with `score < 5`.  
- **Whitespace:** Strip extra spaces from `title`, `author`, and `category`.  
- Convert `collected_at` to datetime.  
- Print the number of rows remaining after cleaning.

### 3 — Save as CSV (6 marks)
- Save the cleaned DataFrame to:  
  `data/trends_clean.csv`  
- Print a confirmation message with the number of rows saved.  
- Print a summary showing how many stories per category remain.

---

## Submission Checklist
- [x] Script runs without errors  
- [x] `data/trends_clean.csv` exists  
- [x] Console shows row count at each step (load, duplicates removed, nulls removed, low-score removed)  
- [x] Stories-per-category summary is printed  
- [x] Code is commented and readable  

---