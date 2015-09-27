import csv
import sys

'''
filecmp: A library that compares files and directories.
From the Python prompt type help(filecmp) to see what it does.
'''
import filecmp

print(sys.version)

with open('./short.csv', 'rb') as file:
    data = csv.DictReader(file)

    with open('./save.csv', 'wb') as output:
        #print(data.fieldnames)
        #print(data.next())
        filter = csv.DictWriter(output, data.fieldnames)
        filter.writeheader()
        filter.writerows(data)

if (filecmp.cmp('./short.csv', './save.csv')):
    print("The input and output files are the same!")
else:
    print("Oops, something went wrong. Try putting in some extra print \
          statements to get a better idea of what's happening.")

