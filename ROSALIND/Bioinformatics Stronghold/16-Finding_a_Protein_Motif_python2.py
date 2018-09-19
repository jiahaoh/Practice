class Solution(object):
    def __init__(self):
        import re
        import urllib
        from Bio import SeqIO
        file = open("rosalind_mprt.txt", "r")
        solution = open("solution.txt", "w")

        id_list = file.read().split()

        seq_dic = {}
        for p_id in id_list:
            url = "http://www.uniprot.org/uniprot/" + p_id + ".fasta"
            fasta_file = urllib.urlopen(url)
            fasta_sequences = SeqIO.parse(fasta_file, 'fasta')
            for fasta in fasta_sequences:
                sequence = fasta.seq
                seq_dic[p_id] = str(sequence)
        fasta_file.close()

        motif = re.compile('(?=N[^P][ST][^P])')

        for k, v in seq_dic.items():
            if re.search(motif, v):
                motif_location = []
                print >>solution, k
                for m in re.finditer(motif, v):
                    motif_location.append(m.start() + 1)
                print >>solution, ' '.join(map(str, motif_location))

Solution()