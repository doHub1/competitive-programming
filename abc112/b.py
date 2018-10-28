# 2 * N の配列 https://beta.atcoder.jp/contests/abc034/submissions/2638960
''' こんな感じ
3
100 15
300 20
200 30
'''


# 数字複数
N, Limit = map(int, input().split())

flag = True

CT = []
for i in range(N):
    c, t = map(int,input().split())
    if t <= Limit:
        CT.append([c,t])
        flag = False
    else:
        pass
if flag == True:
    print('TLE')
    exit()

CT.sort()

print(min(CT)[0])



'''
5 70
7 60
1 80
4 50
2 56
3 55
'''

