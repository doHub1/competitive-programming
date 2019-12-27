#n, m = map(int, input().split())
#L = [int(n) for n in input().split()]

n,m = 5,0
L=3,4,5,3,4

print(n,m,L)

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1 ,n):
            if L[i]**2 + L[j]**2 == L[k]**2 or L[i]**2 == L[j]**2 + L[k]**2 or L[i]**2 + L[k]**2 == L[j]**2:
                #if i!=j and j!=k and k!=i:
                ans += 1
print (ans)




