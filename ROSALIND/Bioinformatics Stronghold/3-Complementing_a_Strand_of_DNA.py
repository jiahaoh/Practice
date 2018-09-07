class Solution:
    def __init__(self):
        file = open("rosalind_revc.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read()

        comp = {"A":"T", "T":"A", "G":"C", "C":"G"}
        print (''.join(filter(None,list(reversed(list(map(comp.get,seq)))))), file=solution)

Solution()