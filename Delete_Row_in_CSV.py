import csv
# Import CSV Modules

# Read CSV File
with open("CSVCodes/AllDetails.csv",'r') as f:
    csvr=csv.reader(f)

found=0
# Found is Boolean

ml=[]
# EMpty Modified list store element not in found result

sno=input("Enter Row's S.No to Modify")

for r in csvr:
    if r[0] != sno:
# Line for Delete Element
      ml.append(r)
    else:
      found=1


if found==0:
    print("Data Not FOund")

else:
    with open("CSVCodes/AllDetails.csv","w",newline="") as f:
        csvw=csv.writer(f)
        csvw.writerows(ml)
        print("File Modified Successfully")
        f.close()
