import csv

with open('SOCR-HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)

newData=[]
for i in range(len(fileData)):
    number=fileData[i][1]
    newData.append(float(number))

count=len(newData)
total=0
for j in newData:
    total=total+j

mean=total/count
print(mean)