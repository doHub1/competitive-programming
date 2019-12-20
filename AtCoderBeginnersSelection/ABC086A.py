x, y = map(int, input().split())

multi= x*y

ans = "Even"

if multi%2:
    ans = "Odd"

print(ans)



