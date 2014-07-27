import MapReduce
import sys

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
    temp2=[]
    temp3=[]
    for v in list_of_values:
        if v[0]=='order':
            temp3.extend(v)
        else:
            temp4=[]
            temp4.extend(temp3)
            temp4.extend(v)
            temp2.append(temp4)
    for i in range(0,len(temp2)):
        mr.emit(temp2[i])
#    mr.emit(temp2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
