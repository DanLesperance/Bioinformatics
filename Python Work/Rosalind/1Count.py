import sys

handle = sys.argv[1]
f = open(handle,'r')
seq = f.read()
A=0
C=0
G=0
T=0
for n in seq:
    if n == 'A':
        A+=1
    elif n=='C':
        C+=1
    elif n =="T":
        T+=1
    elif n =='G':
        G+=1
print(str(A)+' '+str(C)+' '+str(G)+' '+str(T))
