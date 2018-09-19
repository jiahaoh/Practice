class Solution(object):
    def __init__(self):
        file = open("rosalind_fibd.txt", "r")
        solution = open("solution.txt", "w")

        num = file.read().split()
        self.n, self.m = int(num[0]), int(num[1])

        def fib(n,m):
            ages = [1] + [0] * (m - 1)
            for i in range(n - 1):
                ages = [sum(ages[1:])] + ages[:-1]
            return (sum(ages))

        print (fib(self.n, self.m), file = solution)


Solution()