###
Pythonで競技プログラミングする時に知っておきたいtips(入出力編)
https://qiita.com/lethe2211/items/6cbade2bc547649bc040

複数行を配列にまとめる
http://suzu6.hatenablog.com/entry/2017/09/21/032926


Python3の文字列操作
https://qiita.com/Kenta-Han/items/e64035e9c3e4ef08e394



###


# 入力
# 一つの文字列の入力
s = str(input())

# 一つの数字の入力
a = int(input())

# 数字複数
x, y = map(int, input().split())

# 文字列
x, y = map(str, input().split())


# A[n]個の改行のある数値を取得
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
print(A) #サンプル表示


# N個の改行のある文字列を取得
N = int(input())
W = []
for i in range(N):
    W.append(str(input()))
print(W) #サンプル表示


# N個のスペース区切りの数値を取得
N = int(input())
A = [int(N) for N in input().split()]
print (A)



# 2 * N の配列 https://beta.atcoder.jp/contests/abc034/submissions/2638960
''' こんな感じのInput
3
100 15
300 20
200 30
'''
N = int(input())
W,P = [],[]
for i in range(N):
    w,p = map(int,input().split())
    W.append(w)
    P.append(p)
print(W)
print(P)



# 改行あり、スペースあり
### イメージ
N M
a11 a12 a13 ... a1M
a21 a22 a23 ... a2M
a31 a32 a33 ... a3M
...
aN1 aN2 aN3 ... aNM

### 取得方法
N, M = map(int, input().split())
matrix = [[0]*M]*N
for i in range(N):
    matrix[i] = [int(M) for M in input().split()]
print (matrix)

### 入力サンプル
5 7
4 64 8 32 16 2 4
2 16 2 2 4 2 2
32 2 8 8 32 16 32
32 32 32 64 8 2 8
2 8 32 16 16 64 8



###
Python3系の基礎文法（文字列）
https://qiita.com/Amtkxa/items/a03dabe050d8c648f098
###

# for文
for op in ("+","-"):
for i in range(N):
for i in range(len(s)):


# 正規表現
## 検索
import re
address = "hogeasdfa 123-7777 東京都千代田区"
postCode = re.search('[0-9]{3}-[0-9]{4}' , address)
if postCode:
    print (postCode.group(0))

## 
tel = "03-1111-2222"
import re
if re.match('[0-9]{2}-[0-9]{4}-[0-9]{4}', tel):
    print('OK')


## 置換




# 便利関数
## 重複しない要素を抽出(＆ソート)
array = [3, 1, 3, 2]
print(set(array))
#>{1, 2, 3}


