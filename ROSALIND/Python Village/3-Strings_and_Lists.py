class Solution:
    def __init__(self):
        file = open("rosalind_ini3.txt", "r")
        seq = file.read().split()
        #print (seq)
        text = seq[0]
        a,b,c,d = int(seq[1]), int(seq[2])+1, int(seq[3]), int(seq[4])+1
        print(text[a:b] + " " + text[c:d])

Solution()