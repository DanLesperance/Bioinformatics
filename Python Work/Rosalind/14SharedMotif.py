import sys
from Bio import SeqIO

#Read through the file and obtain sequences
file=sys.argv[1]
sequence_mult = []
handle = open(file, 'r')
for rec in SeqIO.parse(handle, 'fasta'):
    sequence = []
    seq = ''
    for nt in rec.seq:
        seq += nt
    sequence_mult.append(seq)
handle.close()


#sort the sequences by len
#check if string in shortest is in the others
sort_seq = sorted(sequence_mult, key=len)
ref = sort_seq[0]#shortest seq, used as reference
comp = sort_seq[1:] #other sequences to check against ref
motif = ''
for i in range(len(ref)):
    for j in range(i, len(ref)):
        m = ref[i:j + 1]
        found = False
        for sequ in comp:
            if m in sequ:
                found = True
            else:
                found = False
                break
        if found and len(m) > len(motif):
            motif = m
print(motif)
