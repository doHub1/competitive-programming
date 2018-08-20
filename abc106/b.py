a = int(input())
ans = 0
for i in range(1,a+1,2):
    #print(i)
    count = 0
    for j in range(1,a+1):
        if i%j==0:
            count += 1
            #print(count,j)
    if count == 8:
        ans += 1
        #print(i,j)
print(ans)

