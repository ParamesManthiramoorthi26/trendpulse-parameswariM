#------------- Task 2 data processing-----------
# import Required Library
import pandas as pd
import json

with open ("/content/trends_20260403.json" , "r") as f :
  post_list = json.load(f)
story_list = pd.DataFrame(post_list)
story_list

# view first 5 rows
story_list.head()

# view last 5 rows
story_list.tail()

story_list.info()

# convert collected_at dtypes as datetime
story_list['collected_at'] = pd.to_datetime(story_list['collected_at'])
# Check the info again
story_list.info()

# check missing values
story_list.isnull().sum()

# Check for duplicates
duplicates = story_list[story_list.duplicated(subset= ['Post_id'])]
print(" Number of Dublicate Rows ",len(duplicates))

# 3. Standardize text columns
story_list['category'] = story_list['category'].str.strip().str.title()
story_list['title'] = story_list['title'].str.strip()
story_list['author'] = story_list['author'].str.strip()

story_list.head()

import os

# Create folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save the dataframe to CSV with current date in the filename
filename = f"data/story_list_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
story_list.to_csv(filename, index=False)

print(f" {filename}  : saved successfully as CSV  ")

