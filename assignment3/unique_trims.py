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
    seqId = record[0]
    dna = str(record[1])
    key = dna[:-10] 
    mr.emit_intermediate(key, 1)

def reducer(dna, list_of_values):
    mr.emit(str(dna))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

