# Task 3 – Data Analysis with Pandas & NumPy

**Project:** TrendPulse — What's Actually Trending Right Now  
---

## Objective
The goal of Task 3 is to **analyze the cleaned dataset from Task 2** using Pandas and NumPy.  
This includes exploring the data, calculating statistics, identifying trends, and adding new analytical columns.  
The final result is saved as a new CSV file for further visualization in Task 4.

---

## Input
- Cleaned CSV file from Task 2:  
  `data/trends_clean.csv`  
- Contains fields:  
  `Post_id`, `title`, `author`, `score`, `num_comments`, `category`, `collected_at`

---

## Tasks

### 1 — Load and Explore (4 marks)
- Load the CSV file into a Pandas DataFrame  
- Display the first 5 rows  
- Print the shape of the DataFrame (rows and columns)  
- Calculate and print:
  - Average score  
  - Average number of comments  

---

### 2 — Basic Analysis with NumPy (8 marks)
Perform statistical analysis on the dataset:
- Calculate:
  - Mean score  
  - Median score  
  - Standard deviation of score  
- Identify:
  - Highest score  
  - Lowest score  
- Find:
  - Category with the most stories  
  - Story with the highest number of comments (print title and comment count)  

---

### 3 — Add New Columns (5 marks)
Add the following calculated columns:

- **Engagement**  
  - Formula: `num_comments / (score + 1)`  
  - Represents how much discussion a story generates per upvote  

- **Is_popular**  
  - True if `score > average score`, otherwise False  
  - Helps identify above-average performing stories  

---

### 4 — Save the Result (3 marks)
- Save the updated DataFrame to:  
  `data/trends_analysed.csv`  
- Print a confirmation message with:
  - Number of rows  
  - Number of columns  

---

