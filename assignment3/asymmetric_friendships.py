import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person=record[0]
    friend = record[1]
    mr.emit_intermediate(person,(person,friend))
    mr.emit_intermediate(friend,(friend,person))

def reducer(key, list_of_values):
    temp=[]
    for v in list_of_values:
        if v in temp:  
            temp.remove(v)
        else:
            temp.append(v)
            
    for v in temp:
        mr.emit(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
