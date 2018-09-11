class Solution (object):
    def __init__(self):
        from Bio import SeqIO
        file = open("rosalind_gc.txt", "r")
        solution = open("solution.txt", "w")

        def GC_content(seq):
            dic_GC = {"G" : 0, "C" : 0}
            length = len(seq)
            for n in seq:
                if n == "G": dic_GC["G"] += (1/length)
                elif n == "C": dic_GC["C"] += (1/length)
            return round(sum(dic_GC.values()) * 100, 6)

        seq_dic = SeqIO.to_dict(SeqIO.parse(file, 'fasta'))
        GC = {}
        for k,v in seq_dic.items():
            GC[k] = GC_content(v.seq)

        print (max(GC, key=GC.get), file=solution)
        print (max(GC.values()), file=solution)


import time
start_time = time.time()
Solution()
print("--- %s seconds ---" % (time.time() - start_time))
