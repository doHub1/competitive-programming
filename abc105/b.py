N = int(input())

ans = "No"

for i in range(0,25):
    for j in range(0,20):
        if 4*i + 7*j == N:
            ans = "Yes"

print(ans)
