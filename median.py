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
newData.sort()
if count%2==0:
    median1=float(newData[count//2])
    median2=float(newData[count//2-1])
    median=(median1+median2)/2

else:
    median=newData[count//2]

print(median)