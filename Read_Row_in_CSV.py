import csv
With open('AllDetails.csv') as f:
#   type(file)

  csvreader=csv.reader(file)
rows=[]
for row in csvreader:
    rows.append(row)

a=len(rows)
print(rows,a)
