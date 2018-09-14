class Solution(object):
    def __init__(self):
        file = open("test.txt", "r")
        solution = open("solution.txt", "w")

        num = file.read().split()
        n, m = int(num[0]), int(num[1])

Solution()