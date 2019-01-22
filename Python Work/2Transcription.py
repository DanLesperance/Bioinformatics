import sys

handle = sys.argv[1]
f = open(handle,'r')
seq= f.read()
seq= list(seq)
for n in range(0,len(seq)):
    if seq[n] =='T':
        seq[n]='U'
print(''.join(seq))