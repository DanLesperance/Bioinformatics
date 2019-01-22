import sys
handle = sys.argv[1]
seq = ''
motif = ''
with open(handle) as seqFile:
    for line in seqFile:
        if seq == '':
            seq =line
        else:
            motif=line
v =''
for i in range(0,len(seq)):
    if seq[i:len(motif)-1+i] == motif[0:-1]:
        v=v+' '+str(i+1)

print(v)