import re

# 一つの文字列の入力
s1 = str(input())

# 一つの文字列の入力
s2 = str(input())

length = len(s1)

for i in range(length):
#    print(i)

    if s1[i] != s2[i]:
#        print('文字が異なる')

        if s1[i] == '@' and re.match('[atcoder]', s2[i]):
#            print('入れ替え可能')
            pass

        elif s2[i] == '@' and re.match('[atcoder]', s1[i]):
#            print('入れ替え可能')
            pass
            
        else:
            print('You will lose')
            exit()

print('You can win')



