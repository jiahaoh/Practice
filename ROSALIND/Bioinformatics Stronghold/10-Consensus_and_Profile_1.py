class Solution (object):
    def __init__(self):
        import numpy as np
        from collections import Counter
        from Bio import SeqIO

        file = open("rosalind_cons.txt", "r")
        solution = open("solution.txt", "w")

        seq = SeqIO.parse(file, 'fasta')
        seq_array = []
        for i in seq:
            rows = []
            rows.append(i.id)
            for n in i.seq:
                rows.append(n)
            seq_array.append(rows)
        seq_matrix = np.matrix(seq_array)

        for n in range(1,len(i.seq)+1):
            x = Counter(str(seq_matrix[:,n])).most_common()
            x = list(filter(lambda x: x[0]!=' ' and x[0]!='\n' and x[0]!="'" and x[0]!='[' and x[0]!=']', x))
            print (x[0][0], end='', file=solution)

        print ('\nA:', end=' ', file=solution)
        for n in range(1,len(i.seq)+1):
            print (str(seq_matrix[:,n]).count("A"), end=' ', file=solution)
        print('\nC:', end=' ', file=solution)
        for n in range(1,len(i.seq)+1):
            print (str(seq_matrix[:,n]).count("C"), end=' ', file=solution)
        print('\nG:', end=' ', file=solution)
        for n in range(1,len(i.seq)+1):
            print (str(seq_matrix[:,n]).count("G"), end=' ', file=solution)
        print('\nT:', end=' ', file=solution)
        for n in range(1,len(i.seq)+1):
            print (str(seq_matrix[:,n]).count("T"), end=' ', file=solution)


import time
start_time = time.time()
Solution()
print("--- %s seconds ---" % (time.time() - start_time))