N = int(input())
a=2
b=1
c=0
if N==1 :
    print(1)
else :
    for i in range(N-1) :
        #print(i,a,b,c)
        c = a + b
        a = b
        b = c
    print(c)
