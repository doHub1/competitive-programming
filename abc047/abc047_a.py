# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
a, b, c = map(int, input().split())

# 出力
#print("{} {}".format(a+b+c))
if a+b==c or a+c==b or b+c==a :
    print("Yes")
else:
    print("No")

