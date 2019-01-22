import sys

handle = sys.argv[1]

obj = open(handle,'r')
seq = obj.read()

aaDict = {'F':2,'L':6,'I':3,'M':1,'V':4,'S':6,'P':4,'T':4,'A':4,
          'Y':2,'H':2,'Q':2,'N':2,'K':2,'D':2,'E':2,'C':2,'W':1,
          'R':6,'G':4}
amt = 1
for aa in seq:
    if aa=='U':
        print('FUCK')
        break
    amt = amt*aaDict.get(aa)
print(amt*3%1000000)
