class Solution (object):
    def __init__(self):
        import re
        file = open("rosalind_subs.txt", "r")
        solution = open("solution.txt", "w")

        seq = file.read().split()
        ref_seq, sub_seq = seq[0], '(?='+seq[1]+')'

        index = [m.start() for m in re.finditer(sub_seq, ref_seq)]

        for i in index:
            print (i + 1, end=' ', file=solution)



Solution()