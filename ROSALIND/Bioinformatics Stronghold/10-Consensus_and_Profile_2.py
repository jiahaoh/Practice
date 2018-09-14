class Solution(object):
    def __init__(self):
        from Bio import SeqIO
        file = open("rosalind_cons.txt", "r")
        solution = open("solution.txt", "w")

        fasta_sequences = SeqIO.parse(file, 'fasta')

        seq_list = []
        for fasta in fasta_sequences:
            name, sequence = fasta.id, fasta.seq
            seq_list.append(str(sequence))

        seq_length = len(seq_list[0])
        con_seq = []
        a_list = []
        t_list = []
        g_list = []
        c_list = []
        for i in range(0, seq_length):
            counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
            a = 0
            for seq in seq_list:
                counts[seq[i]] += 1
            for item in counts:
                if counts[item] == max(counts.values()) and a < 1:
                    con_seq.append(item)
                    a += 1
            a_list.append(counts['A'])
            t_list.append(counts['T'])
            g_list.append(counts['G'])
            c_list.append(counts['C'])

        print (''.join(con_seq), file=solution)
        print ('A:', end=' ', file=solution)
        for num in a_list:
            print (num, end=' ', file=solution)

        print ('\nC:', end=' ', file=solution)
        for num in c_list:
            print (num, end=' ', file=solution)

        print ('\nG:', end=' ', file=solution)
        for num in g_list:
            print (num, end=' ', file=solution)

        print ('\nT:', end=' ', file=solution)
        for num in t_list:
            print (num, end=' ', file=solution)


import time
start_time = time.time()
Solution()
print("--- %s seconds ---" % (time.time() - start_time))