class Solution (object):
    def __init__(self):
        file = open("rosalind_fib.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read().split()

        self.n, self.k = int(seq[0]), int(seq[1])
        #print (self.n, self.k)

        def fib(n,k):
            if n == 1 or n == 2:
                return 1
            elif n == 3:
                return k + 1
            return fib(n - 1, k) + fib(n - 2, k) * k

        print (fib(self.n, self.k), file = solution)


Solution()