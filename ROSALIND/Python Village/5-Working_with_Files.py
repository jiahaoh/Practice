class Solution:
    def __init__(self):
        file = open("rosalind_ini5.txt", "r")
        solution = open("solution.txt", "w")
        text = file.read().split("\n")
        length = len(text)
        new_text = []
        for i in range(1, length, 2):
            new_text.append(text[i])

        for seq in new_text:
            print(seq, file=solution)


Solution()