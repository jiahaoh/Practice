class Solution (object):
    def __init__(self):
        from Bio.Seq import Seq
        from Bio.Alphabet import IUPAC
        file = open("rosalind_prot.txt", "r")
        solution = open("solution.txt", "w")
        seq = file.read()

        m_rna = Seq(seq, IUPAC.unambiguous_rna)
        pro_seq = m_rna.translate(to_stop=True)

        print (pro_seq, file=solution)

Solution()