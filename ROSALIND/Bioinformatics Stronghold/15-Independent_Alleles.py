class Solution(object):
    def __init__(self):
        import Frq_use
        file = open("rosalind_lia.txt", "r")
        solution = open("solution.txt", "w")

        num_list = list(map(int,file.read().split()))
        k, n = num_list[0], num_list[1]

        def men_2nd(k, n):
            p_AaBb = 0.25
            total_p = []
            for i in range(n, (2 ** k) + 1):
                total_p.append(Frq_use.fu.nCk((2 ** k), i) * (p_AaBb ** i) * ((1 - p_AaBb) ** ((2 ** k) - i)))
            return sum(total_p)

        print (men_2nd(k,n), file=solution)


Solution()