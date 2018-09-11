class Solution (object):
    def __init__(self):
        from Bio import SeqIO
        from Bio.SeqUtils import GC
        file = open("rosalind_gc.txt", "r")
        solution = open("solution.txt", "w")

        seq_dic = SeqIO.to_dict(SeqIO.parse(file, 'fasta'))
        GC_dict = {}
        for k,v in seq_dic.items():
            GC_dict[k] = round(GC(v.seq), 6)

        print (max(GC_dict, key=GC_dict.get), file=solution)
        print (max(GC_dict.values()), file=solution)



import time
start_time = time.time()
Solution()
print("--- %s seconds ---" % (time.time() - start_time))