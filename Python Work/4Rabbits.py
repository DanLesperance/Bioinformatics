import sys

month = int(sys.argv[1])
pair = int(sys.argv[2])

a,b = 0,1
for i in range(1,month):
    a,b = b,(pair*a+b)
print(b)