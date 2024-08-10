# Creates an excel file with budget template. This is the bare file with fake data
# Need to add the actual template

# Import the necessary libraries
import openpyxl
import pandas as pd

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Select the default sheet
sheet = workbook.active

# Add data to the Excel sheet
data = [
    ["Name", "Age", "City"],
    ["John", 28, "New York"],
    ["Alice", 24, "San Francisco"],
    ["Bob", 32, "Los Angeles"]
]
for row in data:
    sheet.append(row)

# Save the workbook to a file
workbook.save("C:/Users/vance/Downloads/wig_budget.xlsx")
# Print a success message
print("Excel file created successfully!")
