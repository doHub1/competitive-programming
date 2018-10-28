# 一つの文字列の入力
s = str(input())

if len(s) == 2:
    print(s)
else:
    print(s[2]+s[1]+s[0])