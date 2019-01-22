import sys
from Bio import SeqIO

handle = sys.argv[1]

seq=''
pat=''

for seqRec in SeqIO.parse(handle,'fasta'):
    if seq=='':
        seq=seqRec.seq
    else:
        pat=seqRec.seq

match=''
lastmatch = 0
for L in pat:
    for b in range(len(seq)):
        if L == seq[b]:
            if lastmatch<b:
                lastmatch = b
                match = match + ' ' + str(b + 1)
                break
print(match)
