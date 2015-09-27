import csv
import sys


with open('./short.csv', 'rb') as file:
    data = csv.DictReader(file)

    with open('./save.csv', 'wb') as output:
        #print(data.fieldnames)
        #print(data.next())
        filter = csv.DictWriter(output, data.fieldnames)
        filter.writeheader()
        filter.writerows(data)

print("Done")
