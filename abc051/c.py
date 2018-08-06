sx, sy, tx, ty = map(int, input().split())

yoko = tx - sx
tate = ty - sy

ans1 = ""
ans2 = ""

ans2 += "LU"

for i in range(tate):
    ans1 += "U"
    ans2 += "U"
for i in range(yoko):
    ans1 += "R"
    ans2 += "R"

ans2 +="RDRD"

for i in range(tate):
    ans1 += "D"
    ans2 += "D"
for i in range(yoko):
    ans1 += "L"
    ans2 += "L"

ans2 += "LU"

print(ans1 + ans2)

