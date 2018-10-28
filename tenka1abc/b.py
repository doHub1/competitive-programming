A,B,K = map(int, input().split())

for i in reversed(range(K,0,-1)):

    if i%2 == 1:
        #Aの処理
        if A%2 == 1:
            A=A-1
        A=int(A/2)
        B=B+A
#        print("RES_A: " + str(A) + str(B) )

    else:
        #Bさん
        if B%2 == 1:
            B=B-1
        B=int(B/2)
        A=A+B
#        print("RES_B: " + str(A) + str(B))

print(A, B)
