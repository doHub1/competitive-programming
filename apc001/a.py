x, y = map(int, input().split())


if x % y == 0:
    print(-1)

else:
    for i in range(2,100000000000000000):
        if (x*(i))%y != 0:
            print(x*((i)))
            break
            
