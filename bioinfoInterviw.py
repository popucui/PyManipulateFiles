import os, sys
import re

def countGC(seq):
  '''return GC percent of given seq. Since Ns are ambiguous base, they are not included

  '''
  total = seq.count('A') + seq.count('T') + seq.count('C') + seq.count('G')
  gc = seq.count('C') + seq.count('G')
  return round( (float(gc) / total) * 100 )


if __name__ == '__main__':
  wdir = sys.argv[1]
  wdir = os.listdir(wdir)
  # result to hold all elements with FileName, sequence name and GC percent
  result = []
  for file in wdir:
    with open(file) as f:
      firstline = f.readline()
      match = re.search(r'^>', firstline)
      if match:
#      if '>' in firstline:
        #first line begin with '>', then this is fasta file
        #first extract the sequence name from firstline, those left are seq
        seqname = firstline[1:].strip()
        seq = f.readlines()
        gc = countGC(''.join(seq))
        t = (file, seqname, gc)
        result.append(t)
        
#sort list by GC content.
  result = sorted(result, key = lambda res: res[2])
  with open('report.txt', 'a') as f:
    for t in result:
      line = t[0] + '\t' + t[1] + '\t' + str(t[2]) + '%\n' 
      f.write(line)
    print "totally %s files processed in %s" % (len(result), os.getcwd())
