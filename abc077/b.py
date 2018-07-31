IN = input()
IN = int(IN)

i = 1

for i in range(100000):
    if i**2 > IN:
        print((i-1)**2)
        break
