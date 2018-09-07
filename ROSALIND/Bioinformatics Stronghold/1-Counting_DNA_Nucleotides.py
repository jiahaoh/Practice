class Solution:
    def __init__(self):
        file = open("rosalind_dna.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read()
        dic = {}
        for n in seq:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        print(dic["A"], dic["C"], dic["G"], dic["T"], file = solution)

Solution()