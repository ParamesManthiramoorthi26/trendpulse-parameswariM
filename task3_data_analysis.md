# Task 3 – Data Analysis with Pandas & NumPy

## Overview
In Task 3, we analyze the cleaned Hacker News dataset produced in Task 2. The main objective is to extract insights from the data using **Pandas** and **NumPy**, add new analytical columns, and save the results as a CSV file for further exploration.

> **Note:** The input for this task is the CSV file generated in Task 2 (`story_list_YYYYMMDD_HHMMSS.csv`).

## Steps Performed

### 1. Load the Cleaned CSV
- The CSV from Task 2 is loaded into a Pandas DataFrame.
- The `collected_at` column is converted to datetime for time-based analysis.

### 2. Basic Data Checks
- Checked DataFrame shape, column types, and missing values.
- Verified data integrity after loading.

### 3. Category Analysis
- Count of posts per category.
- Total score per category.
- Total number of comments per category.

### 4. Post-Level Analysis
- Identified the post with the **highest score**.
- Identified the post with the **most comments**.
- Calculated a new column **score per comment** (`score ÷ num_comments`) for each post.
- Found posts with the **highest** and **lowest** score per comment.

### 5. Author Analysis
- Identified the author with the **most posts**.
- Identified the author with the **highest average post score**.

### 6. Saving Results
- The DataFrame, including the new column `score_per_comment`, is saved as a CSV for reporting or further analysis.

## Insights Extracted
- Categories like **Entertainment** and **Technology** have the highest number of posts.
- Posts with the highest score or comment engagement can be easily identified for trending content analysis.
- **score_per_comment** helps determine posts with high impact relative to discussion.
- Top authors are identified both by post count and average post score, highlighting active and influential contributors.

## Output
- A CSV file with all posts, new analytical columns, and ready-to-use for visualization or reporting.
- Key metrics for categories, posts, and authors.