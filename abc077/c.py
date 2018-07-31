import bisect

N = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

A.sort()
C.sort()

count=0
i=0
for i in range(N):
    countA = bisect.bisect_left(A, B[i])
    #print(bisect.bisect_left(A, B[i]))

    countB = N - bisect.bisect_right(C, B[i])
    #print(bisect.bisect_right(C, B[i]))

    count += countA * countB

print(count)
