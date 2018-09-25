# N個のスペース区切りの数値を取得
N = int(input())
A = [int(N) for N in input().split()]

#print (A)

count = 0
sum  = 0
import math

for i in range(N):
    sum += A[i]

    if A[i] == 0:
        count += 1

#print('total:', sum)

print(math.ceil(sum / (N - count)))

