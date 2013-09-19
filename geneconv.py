
if __name__ == "__main__":
    
    with open('inputgene.txt','r') as f:
        genelist = f.readlines()
    i = 0 #count num of query hits
    for g in genelist:      
        q = 'ath:' + g.strip()
        with open('output.txt','a') as f:            
            f.write(q)
            f.write('\n')

    print "convertion complete!"

