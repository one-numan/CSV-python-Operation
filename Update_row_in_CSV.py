import csv
with open("AllDetails.csv",'r') as f
    csvr=csv.reader(f)

found=0
# Found is Boolean

ml=[]
# EMpty Modified list store element not in found result

sno=input("Enter the S.No to Modify")

for r in csvr:
  if (r[0]==sno):
    r[1]=input("1st")
    r[2]=input("2nd")
    r[3]=input("3rd")
    r[4]=input("4th")   
    print(r)
        
    found=1
    ml.append(r)
  
# Line for Delete Element
        
if found==0:
  print("Data Not FOund")

  else:
    with open("AllDetails.csv","w",newline="") as f:
      csvw=csv.writer(f)
      csvw.writerows(ml)
      print("File Modified Successfully")
      f.close()
    
