import math
import sys
k = int(sys.argv[1])
n = int(sys.argv[2])
p = 2**k
ans = 0
for i in range(n, p + 1):
    prob = (math.factorial(p) /(math.factorial(i) * math.factorial(p - i))) * (0.25**i) * (0.75**(p - i))
    ans += prob
print(ans)
