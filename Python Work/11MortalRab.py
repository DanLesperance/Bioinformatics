import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

pairs = [1] + [0]*(m-1)
print(pairs)
for i in range(n-1):
    pairs = [sum(pairs[1:])] + pairs[:-1]
    print(pairs)
print(sum(pairs))
