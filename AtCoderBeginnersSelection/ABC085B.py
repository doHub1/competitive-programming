# A[n]個の改行のある数値を取得
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))


print(len(set(A)))

