class Solution:
    def __init__(self):
        file = open("rosalind_ini6.txt", "r")
        solution = open("solution.txt", "w")
        text = file.read().split()
        dic = {}
        for letter in text:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        for k,v in dic.items():
            print (k,v, file=solution)

Solution()