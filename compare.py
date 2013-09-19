import sys

dfgnlist1 = sys.argv[1]
dfgnlist2 = sys.argv[2]
with open(dfgnlist2, 'r') as deg:
  dfgn2 = deg.readlines()
with open(dfgnlist1,'r') as de:
  dfgn1 =de.readlines()

i = 0
j = 0
for g in dfgn1:
  if g in dfgn2:
    with open("samegenes.txt",'a') as samegenes:
      samegenes.write(g)
      i += 1
  else:
    with open("dfgenes.txt",'a') as dfgenes:
      dfgenes.write(g)
      j += 1

print '========'
print i, 'same genes'
print j, 'different genes'
