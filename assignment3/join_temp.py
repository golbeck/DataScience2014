import json
import pandas as pd
from pandas import DataFrame

inputdata=open("data/records.json")
k1=0
k2=0
order_df=DataFrame()
line_item_df=DataFrame()
for line in inputdata:
    record=json.loads(line)
    temp2=[record[i].encode('utf8') for i in range(0,len(record))]
    if temp2[0]=='line_item':
        line_item_df[temp2[1]]=temp2[2:]
        k1+=1
    else:
        order_df[temp2[1]]=temp2[2:]
        k2+=1
        
temp=pd.merge(order_df,line_item_df,how='outer')
