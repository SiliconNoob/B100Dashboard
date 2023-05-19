import csv

field_names = ["No", "Company"]

cars = [
{"No": 1, "Company": "Ferrari"},
{"No": 2, "Company": "Porsche"},
{"No": 3, "Company": "Bugatti"},
{"No": 4, "Company": "Rolls Royce"},
{"No": 5, "Company": "BMW"},
]

with open('B200_weekly/Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)