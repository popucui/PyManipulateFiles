import re
with open('uniportlist.txt','r') as f:
    genelist = f.readlines()

for g in genelist:      
    g = g.strip()
    unip = re.search(r'\t(\S+)',g)
    h = unip.group(0).strip()
    with open('cleanlist.txt','a') as f:            
        f.write(h)
        f.write('\n')

print 'transform done!'
