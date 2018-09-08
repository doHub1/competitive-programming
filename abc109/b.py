# N個の改行のある文字列を取得
N = int(input())
W = []
for i in range(N):
    W.append(str(input()))
#print(len(W))

if len(W) != len(set(W)):
    print('No')
    exit()

for i in range(N-1):
    #print(W[i], W[i+1])
    if W[i][-1] != W[i+1][0]:
        print('No')
        exit()

print('Yes')


