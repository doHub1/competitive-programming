n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
print(s[0])

total = 0
for i in range(n):
    total += s[i]

if total%10 != 0:
    print(total)

else:
    print("not")

