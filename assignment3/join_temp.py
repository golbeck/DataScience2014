import json
from pandas import DataFrame

inputdata=open("data/records.json")
temp3=[]
for line in inputdata:
    record=json.loads(line)
    temp2=[record[i].encode('utf8') for i in range(0,len(record))]
    temp3.append(temp2)
    
df=DataFrame(temp3)
    
inputdata=open("solutions/join.json")
temp3=[]
for line in inputdata:
    record=json.loads(line)
    temp2=[record[i].encode('utf8') for i in range(0,len(record))]
    temp3.append(temp2)
    
df=DataFrame(temp3)
