N,M,A,B = map(int, input().split())

L,R = [],[]
for i in range(M):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
#print(L)
#print(R)


# 値がB、長さNの配列を用意する
array = [B] * N
#print(array)


for i in range(M):
    for j in range(1,N+1):
        if L[i] <= j and j <= R[i] :
#            print('replace')
            array[j-1] = A
#        else:
#            print('No')
#        print('now:', array)

print(sum(array))





