class Solution (object):
    def __init__(self):
        file = open("rosalind_hamm.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read().split()

        count = 0
        for i in zip(seq[0], seq[1]):
            if i[0] != i[1]:
                count += 1

        print (count, file=solution)

Solution()