import sys

handle=sys.argv[1]

with open(handle,'r') as f:
    sequences=f.readlines()

seq1=sequences[0]
seq2=sequences[1]
count=0
for n in range(0,len(seq1)-1):
    if seq1[n]!=seq2[n]:
        count+=1
print(count)