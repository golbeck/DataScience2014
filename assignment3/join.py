import MapReduce
import sys
import pandas as pd
from pandas import DataFrame

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
    attributes = record[2:]
    mr.emit_intermediate(order_id,attributes)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    temp=DataFrame()

#    temp.append(key)
    for v in list_of_values:
        
    temp2=[record[i].encode('utf8') for i in range(0,len(record))]
        temp.append(v)
    mr.emit((key, temp))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
