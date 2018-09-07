class Solution:
    def __init__(self):
        file = open("rosalind_rna.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read()
        rna_seq = []
        for n in seq:
            if n == "T":
                rna_seq.append("U")
            else:
                rna_seq.append(n)

        print(''.join(rna_seq), file=solution)

Solution()