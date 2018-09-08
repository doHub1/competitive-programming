import functools
import fractions

N, X = map(int, input().split())
x = [int(i) for i in input().split()]

if N == 1:
    print(abs(x[0] - X))
    exit()

x.append(X)
x.sort()
#print(x)

dist = []
for i in range(N-1):
    dist.append(abs(x[i] - x[i+1]))

gcd = functools.reduce(fractions.gcd, dist)
print(gcd)



