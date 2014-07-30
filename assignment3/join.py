import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""
mr = MapReduce.MapReduce()
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #key = record[1]
    #valueList = record
    mr.emit_intermediate(int(record[1]), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print str(key)+' '+str(len(list_of_values)) 
    #mergedList=[] 
    first = list_of_values[0]
    global total 
    for i in range(len(list_of_values)):
       if i>0: 
          print i 
          mr.emit((first + list_of_values[i])) 
    #print len(mergedList)  
    #mr.emit(total)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

