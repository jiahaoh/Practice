class Solution:
    def __init__(self):
        file = open("rosalind_ini4.txt", "r")
        seq = file.read().split()
        a = int(seq[0])
        b = int(seq[1])
        sum = 0
        for i in range(a,b+1):
            if i % 2 == 0:
                pass
            else:
                sum += i
        print (sum)
        
Solution()