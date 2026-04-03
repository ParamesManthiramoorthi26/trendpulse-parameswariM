# Task 2 – Data Processing

## Objective
The goal of this task is to process and clean the raw data collected from Hacker News in **Task 1**. The JSON file generated in Task 1 serves as the input for this task. The data is cleaned and saved as a CSV file for further analysis.

## Steps Performed

1. **Load JSON Data**
   - The JSON file containing Hacker News stories collected in Task 1 is read into a Pandas DataFrame.

2. **Data Cleaning & Transformation**
   - Convert the `collected_at` column to a `datetime` datatype for proper time-based handling.
   - Check for and handle any missing values or duplicate rows.
   - Standardize text columns:
     - Remove extra spaces from `title`, `author`, and `category`.
     - Ensure consistent capitalization in `category`.

3. **Save Cleaned Data**
   - The cleaned DataFrame is saved as a CSV file in the `data/` folder.
   - The filename includes a timestamp to ensure versioning and easy identification, e.g., `data/story_list_YYYYMMDD_HHMMSS.csv`.

## Output
- A cleaned CSV file with the following columns:
  1. `Post_id` – Unique ID of the story.
  2. `title` – Story title.
  3. `author` – Username of the poster.
  4. `score` – Number of upvotes.
  5. `num_comments` – Number of comments.
  6. `category` – Category assigned based on keywords.
  7. `collected_at` – Date and time when the story was collected.

- This CSV dataset is now ready for **Task 3 – Data Analysis**.

## Notes
- The `data/` folder is automatically created if it does not exist.
- The cleaning ensures consistency, no missing values, and no duplicates.
- **Task 1 output (JSON file) is the input for this task**, ensuring a seamless workflow.