import MapReduce
import sys
import pandas as pd
from pandas import DataFrame, Series

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # table: table that the record originates from
    # order_id: order id number
#    table = record[0]
    order_id=record[1]
    attributes = record
    mr.emit_intermediate(order_id,attributes)

def reducer(key, list_of_values):
    
    line_item_df=DataFrame()
    order_df=DataFrame()
    
    for v in list_of_values:
        if v[0]=='line_item':
            line_item_df[v[1]]=v
        else:
            order_df[v[1]]=v
        
    temp=pd.concat([order_df,line_item_df])
    temp4=[list(x) for x in temp.T.itertuples()]
    mr.emit((key, temp4[0][1:]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
