"""
Your module description
"""
import csv

 

# Data to write to the CSV file

data = [

    ['Name', 'Age', 'Location'],

    ['Alice', 25, 'New York'],

    ['Bob', 30, 'San Francisco'],

    ['Charlie', 22, 'Los Angeles']

]

 

# Open the CSV file for writing

with open('output.csv', 'w', newline='') as file:

    # Create a CSV writer object

    csv_writer = csv.writer(file)

    

    # Write the data to the CSV file row by row

    for row in data:

        csv_writer.writerow(row)