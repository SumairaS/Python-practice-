"""
Your module description
"""
import csv

# Open the CSV file for reading

with open('data.csv', 'r') as file:

    # Create a CSV reader object

    csv_reader = csv.reader(file)

    

    # Iterate through each row in the CSV file

    for row in csv_reader:

        # Each row is a list of values

        print(row)