s = str(input())
k = int(input())

ans = 1
for i in range(k):
    #print("hoge")
    if s[i] != "1":
        ans = s[i]
        break
print(ans)

