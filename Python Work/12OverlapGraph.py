import sys
handle = sys.argv[1]



from Bio import SeqIO


def adjList(k, handle):
    seqs = list(SeqIO.parse(handle, "fasta"))


    for value in range(len(seqs) - 1):
        for inVal in range(len(seqs)):
            if str(seqs[value].seq) != str(seqs[inVal].seq):
                if str(seqs[value].seq[:k]) == str(seqs[inVal].seq[-k:]):
                    print(" ".join([seqs[inVal].id, seqs[value].id]))
            else:
                continue



k = 3


adjList(k, handle)