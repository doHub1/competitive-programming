k, s = map(int, input().split())

count = 0

for i in range(k+1):
    #print("i=" + str(i))
    x = i
    for j in range(k+1):
        #print("j=" + str(j))
        y = j
        for k in range(k+1):
            #print("k=" + str(k))
            z = k
            #print(x,y,z,s)
            #print("----------")
            if x + y + z == s:
                count += 1

        

print(count)
