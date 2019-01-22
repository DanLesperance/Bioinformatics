import sys
from Bio import SeqIO

handle = sys.argv[1]
Scaf=''
GC=0
count=1
l=0
for seq_rec in SeqIO.parse(handle,'fasta'):
    gc=0
    seq=seq_rec.seq
    for n in seq:
        if n in 'GC':
            gc+=1
    if count==1:
        GC =gc
        Scaf=seq_rec.id
        l=len(seq_rec.seq)
    elif gc>GC:
        GC=gc
        Scaf=seq_rec.id
        l=len(seq_rec.seq)
    count+=1
content = (GC/l)*100
print(Scaf)
print(content)
