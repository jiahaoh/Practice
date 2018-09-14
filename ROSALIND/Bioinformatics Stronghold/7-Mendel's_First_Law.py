class Solution (object):
    def __init__(self):
        import math
        file = open("rosalind_iprb.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read().split()
        k,m,n = int(seq[0]), int(seq[1]), int(seq[2])

        def nCk(n, k):
            f = math.factorial
            return f(n) / f(k) / f(n - k)

        numer = nCk(m, 2) + nCk(n, 2) * 4 + (m * n * 2)
        denom = nCk(k + m + n, 2) * 4

        print (1 - float(numer) / denom, file=solution)

Solution()