import os

# -----------------------------
# List of tasks in order
tasks = [
    "task1_data_collection.py",
    "task2_data_processing.py",
    "task3_analysis.py",
    "task4_visualization.py"
]

# -----------------------------
# Run tasks one by one
for task in tasks:
    print(f"\n================ Running {task} =================")
    ret = os.system(f"python {task}")
    if ret != 0:
        print(f"❌ Error occurred while running {task}. Pipeline stopped.")
        break
    else:
        print(f"✅ {task} completed successfully.")