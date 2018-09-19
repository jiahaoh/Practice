class Solution(object):
    def __init__(self):
        from Bio import SeqIO
        file = open("rosalind_grph.txt", "r")
        solution = open("solution.txt", "w")

        on = 3
        seq_dic = SeqIO.to_dict(SeqIO.parse(file, 'fasta'))
        for k, v in seq_dic.items():
            suffix = v.seq[-on:]
            for k2, v2 in seq_dic.items():
                if v2.seq.startswith(suffix) and v2.seq != v.seq:
                    print (k, k2, file=solution)



Solution()