import sys
import random
import math

x = int(sys.argv[1])
pop = range(1,x+1)

samples= []
for i in range(0,100000):
    samples.append(str(random.sample(pop,x)))
trueAns = math.factorial(x)


def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

ans = sort_and_deduplicate(samples)
if len(ans)==trueAns:
    print(len(ans))
    samples = '\n'.join(ans)
    samples = samples.replace(',',' ')
    samples= samples.replace('[','')
    samples = samples.replace(']','')
    print(samples)
