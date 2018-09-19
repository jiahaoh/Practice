class Solution(object):
    def __init__(self):
        from Bio import SeqIO
        file = open("rosalind_lcsm.txt", "r")
        solution = open("solution.txt", "w")

        seq_list = [i.seq for i in SeqIO.parse(file, 'fasta')]

        lengths = [map(len, seq_list)]
        index = lengths.index(min(lengths))
        seq_min = seq_list[index]

        motif = ''
        motif_list =[]
        for a in range(0, 1000):
            for b in range(1000, a, -1):
                if len(seq_min[a:b]) >= len(motif):
                    count = 0
                    for seq in seq_list:
                        if seq_min[a:b] in seq:
                            count += 1
                        else:
                            break
                    if count == len(seq_list):
                        motif = seq_min[a:b]
                        if motif not in motif_list:
                            motif_list.append(motif)
                            motif_list = list(filter(lambda x: len(x) == len(motif), motif_list))
                else:
                    break

        print (motif_list[0], file=solution)


import time
start_time = time.time()
Solution()
print("--- %s seconds ---" % (time.time() - start_time))