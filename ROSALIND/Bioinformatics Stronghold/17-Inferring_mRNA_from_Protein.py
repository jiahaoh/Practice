class Solution (object):
    def __init__(self):
        from Bio.Data import CodonTable
        file = open("rosalind_mrna.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read().split()

        codon_table = CodonTable.standard_rna_table.forward_table

        num = 1
        for i in seq[0]:
            mult_p = list(codon_table.values()).count(i)
            num *= mult_p

        print (num*3%1000000, file=solution)

Solution()