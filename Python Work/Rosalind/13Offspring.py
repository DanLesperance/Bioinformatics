import sys

Dom = 2* (float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3]))
hetero = 2*.75*float(sys.argv[4])
heteroRec = 2*.5*float(sys.argv[5])

total = Dom+hetero+heteroRec
print(total)
