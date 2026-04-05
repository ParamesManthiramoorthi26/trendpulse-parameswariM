#------------- Task 2 data processing-----------

## Task 2 — Clean the Data & Save as CSV

### 1 — Load the JSON File
"""
# import Required Library
import pandas as pd
import json

# Load the JSON File
with open ("/content/data/trends_20260404.json" , "r") as f :
  post_list = json.load(f)
story_list = pd.DataFrame(post_list)
story_list

# Print how many rows were loaded
print("No of Rows :",story_list.shape[0])
print("No of Columns :",story_list.shape[1])

# view first 5 rows
story_list.head()

# view last 5 rows
story_list.tail()

"""### 2. Clean the Data"""

# Check for duplicates
duplicates = story_list[story_list.duplicated(subset= ['Post_id'])]
print(" Number of Dublicate Rows ",len(duplicates))

# Missing values — drop rows where post_id, title, or score is missing
# check missing values
story_list.isnull().sum()

# Data types — make sure score and num_comments are integers
story_list.dtypes

# Whitespace — strip extra spaces from the title column
# 3. Standardize text columns
story_list['category'] = story_list['category'].str.strip().str.title()
story_list['title'] = story_list['title'].str.strip()
story_list['author'] = story_list['author'].str.strip()

story_list.info()

# convert collected_at dtypes as datetime
story_list['collected_at'] = pd.to_datetime(story_list['collected_at'])
# Check the info again
story_list.info()

# Remove low-quality stories (score < 5)
high_quality_story_list = story_list[story_list['score'] >= 5]
high_quality_story_list

# Print the number of stories per category
print("Stories per category:")
print(high_quality_story_list['category'].value_counts())

"""### 3 — Save as CSV"""

import os

# Create folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save the dataframe to CSV with current date in the filename
filename = f"data/story_list_clean_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
high_quality_story_list.to_csv(filename, index=False)

print(f" {filename}  : saved successfully as CSV  ")

