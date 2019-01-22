import sys
from Bio import SeqIO

handle = sys.argv[1]
f = open(handle,'r')
seq = f.readlines()
for seq_rec in SeqIO.parse(handle,'fasta'):
    A = [0]*len(seq_rec.seq)
    C = [0]*len(seq_rec.seq)
    G = [0]*len(seq_rec.seq)
    T = [0]*len(seq_rec.seq)

for seq_rec in SeqIO.parse(handle,'fasta'):
    for i in range(0,len(seq_rec.seq)):
        if seq_rec.seq[i]=='A':
            A[i]+=1
        elif seq_rec.seq[i]=='G':
            G[i]+=1
        elif seq_rec.seq[i]=='C':
            C[i]+=1
        elif seq_rec.seq[i]=='T':
            T[i]+=1
sequence = []
for n in range(0,len(A)):
    if A[n]>G[n] and A[n]>C[n] and A[n]>T[n]:
        sequence.append('A')
    elif G[n]>C[n] and G[n]>T[n]:
        sequence.append('G')
    elif C[n]>T[n]:
        sequence.append('C')
    else:
        sequence.append('T')



A = str(A).replace(',',' ').replace('[','').replace(']','')
C = str(C).replace(',',' ').replace('[','').replace(']','')
G = str(G).replace(',',' ').replace('[','').replace(']','')
T = str(T).replace(',',' ').replace('[','').replace(']','')
print(''.join(sequence))
print('A:',A)
print('C:',C)
print('G:',G)
print('T:',T)


