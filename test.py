import csv
with open('locations.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print your_list[0][-1].split("(")[0].strip()[:-1]
