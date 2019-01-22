import sys

k = float(sys.argv[1])
m = float(sys.argv[2])
n = float(sys.argv[3])
x=k+m+n

D = ((x-1)*k)+(k*(x-k))
print (D)

DH = (m*(((m-1)*.75) + (n*.5)))
print(DH)

DR = (n*(m*.5))
print(DR)

total = D+DH+DR
print(total/(x*(x-1)))
