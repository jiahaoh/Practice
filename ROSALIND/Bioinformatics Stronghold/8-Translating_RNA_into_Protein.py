class Solution (object):
    def __init__(self):
        file = open("rosalind_prot.txt", "r")
        solution = open("solution.txt", "w")
        codon_file = open("codon_table.txt", "r").read()
        seq = file.read()
        codon_list = codon_file.split()

        codon_dict = {}
        for i in range(0, len(codon_list), 2):
            codon_dict[codon_list[i]] = codon_list[i+1]

        pro_list = [seq[i:i+3] for i in range(0, len(seq)-3, 3)]
        pro = ''.join(filter(lambda x: x!="Stop",list(map(codon_dict.get, pro_list))))
        print (pro, file=solution)


Solution()