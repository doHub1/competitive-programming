n = int(input())
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]

nume = 0
deno = 0

for i in range(n):
    if a[i] > b[i]:
        nume += a[i] - b[i]
    else:
        deno += b[i] - a[i]

if nume*2 <= deno:
    print("Yes")
else:
    print("No")


