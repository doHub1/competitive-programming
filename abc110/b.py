# 数字複数
N,M,X,Y = map(int, input().split())

# スペース区切りの整数N個の入力
x = [int(N) for N in input().split()]
y = [int(M) for M in input().split()]

x.append(X)
y.append(Y)

#print('---')
#print(max(x),min(y))

if max(x) < min(y):
    print('No War')
else:
    print('War')    




