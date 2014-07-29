import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    identifier=record[0]
    row = record[1]
    column = record[2]
    value = record[3]
    if identifier=="a":
        for i in range(0,5):
            mr.emit_intermediate((row,i),[identifier,column,value])
    else:
        for i in range(0,5):
            mr.emit_intermediate((i,column),[identifier,row,value])
        
def reducer(key, list_of_values):
    a_row={}
    b_col={}
    for x in list_of_values:
        if x[0]=="a":
            a_row[str(x[1])]=x[2]
        else:
            b_col[str(x[1])]=x[2]
    v=0
    for x in a_row.keys():
        if x in b_col.keys():
            v+=a_row[x]*b_col[x]
    
    row_new=key[0]
    col_new=key[1]
    mr.emit((row_new,col_new,v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
