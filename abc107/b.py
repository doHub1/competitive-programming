import copy

H, W = map(int, input().split())

a = [input() for _ in range(H)]
ans = copy.deepcopy(a)

print(a)

for i in range(H):
    print("i:", i)

    if a[i].count("#") == 0:
        print("hit")
        #ans = ans.pop(i)
        print("ans:", ans)


print("ans:", ans)
ans.append('hoge')
print("ans:", ans)
print("a  :", a)

