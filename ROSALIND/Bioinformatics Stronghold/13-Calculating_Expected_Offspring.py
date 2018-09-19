class Solution(object):
    def __init__(self):
        file = open("rosalind_iev.txt", "r")
        solution = open("solution.txt", "w")

        num_list = list(map(int, file.read().split()))
        exp_list = [1,1,1,0.75,0.5,0]

        exp_sum = [num_list[i] * exp_list[i] for i in range(len(num_list))]

        print (sum(exp_sum)*2, file=solution)


Solution()