#ABC085C - Otoshidama
import sys

# 数字複数
N, Y = map(int, input().split())

for i in range(0,N+1):
    for j in range(N-i+1):
        k = N-i-j
        if 10000*i + 5000*j + 1000*k == Y:
            print(i, j, k)
            sys.exit()

print('-1 -1 -1')
    





