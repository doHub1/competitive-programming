https://qiita.com/lethe2211/items/6cbade2bc547649bc040

# スペース区切りの整数の入力
a, b, c = map(int, input().split())

# スペース区切りの整数x個の入力
A = [int(x) for x in input().split()]

# 数字複数
x, y = map(int, input().split())

# 文字列
x, y = map(str, input().split())

# 一つの文字列の入力
s = str(input())

# 一つの数字の入力
a = int(input())

# A[n]個の改行のある入力を取得
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
print(s[0])

# 2 * N の配列 https://beta.atcoder.jp/contests/abc034/submissions/2638960
###
3 5
100 15
300 20
200 30
###
N,K = map(int,input().split())
W,P = [],[]
for i in range(N):
    w,p = map(int,input().split())
    W.append(w)
    P.append(p)
print(W)
print(P)



# 改行あり、スペースあり
###
N M
a11 a12 a13 ... a1M
a21 a22 a23 ... a2M
a31 a32 a33 ... a3M
...
aN1 aN2 aN3 ... aNM
###
N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(map(int, input().split()))
print a



# for文
for op1 in ("+","-"):
for i in range(N-1) :
for i in range(len(s)):



