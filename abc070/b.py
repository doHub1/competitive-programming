s = str(input())

count = 0
ans = "yes"
for i in range(len(s)):
    if s.count(s[i]) > 1:
        ans = "no"

print(ans)


