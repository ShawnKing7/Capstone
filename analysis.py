import pandas as pd

# Load the exported dataset
file_path = "C:\\Users\\shawn\\OneDrive\\Desktop\\D502_Capstone\\Task_3\\NTSB_Clean.xlsx"   # File path
df = pd.read_excel(file_path)

# Preview the first few rows
print(df.head())
print(df.columns)
