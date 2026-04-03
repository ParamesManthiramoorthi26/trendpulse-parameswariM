# Task 4 – Data Visualization with Matplotlib & Dashboard

## Overview

In Task 4, we create visualizations from the analyzed Hacker News dataset (produced in Task 3). The goal is to provide clear insights through charts, making it easier to understand post trends, category performance, and author activity.

Additionally, we build a **dashboard PNG** that combines multiple visualizations and KPIs for a single-glance view.

**Input:** `trends_analysed.csv` from Task 3  
**Output:** Three PNG charts + one dashboard PNG saved in the `outputs/` folder.

---

## Steps Performed

### 1. Load Data
- Read the cleaned and analyzed CSV from Task 3 into a Pandas DataFrame.

### 2. Prepare Individual Visualizations
- **Chart 1:** Top posts by score – bar chart showing posts with the highest scores.  
- **Chart 2:** Posts per category – bar chart visualizing the number of posts in each category.  
- **Chart 3:** Scatter plot – post scores vs. number of comments to see engagement trends.  
- **Customizations:** Titles, axis labels, color schemes, legends for clarity.  
- Each chart saved as a PNG file in `outputs/`.

### 3. Create Dashboard
- **Dashboard Layout:**  
  - **Top section:** 4 KPI boxes (Total Posts, Total Comments, Top Score, Top Author)  
  - **Bottom section:** 2x2 subplots showing the 4 charts:  
    - Pie chart: Category Distribution  
    - Bar chart: Posts per Category  
    - Line chart: Top 10 Scores Trend  
    - Scatter chart: Score vs Comments  
- **Enhancements:**  
  - Subplot background colors for readability  
  - Borders around each subplot  
  - Dashboard title added at the top  
- **Saved Output:** `dashboard.png` in the `outputs/` folder

---

## Insights Extracted
- **Top Posts:** Identify the most popular posts by score.  
- **Category Trends:** Determine which categories (e.g., Technology, Entertainment) have the most posts.  
- **Engagement Patterns:** Analyze which posts generate the most discussion relative to score using the scatter plot.  
- **Top Authors & KPIs:** Dashboard highlights top authors, total posts, and key statistics in one glance.

---

## Output Files

| File Name               | Description                                           |
|-------------------------|-------------------------------------------------------|
| chart1_top_posts.png     | Bar chart of top posts by score                       |
| chart2_subreddits.png    | Bar chart of number of posts per category            |
| chart3_scatter.png       | Scatter plot of score vs. number of comments         |
| dashboard.png            | Combined dashboard with KPI tiles and 4 visualizations |