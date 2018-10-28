# A[n]個の改行のある数値を取得
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
# print(A)

A.sort()
print(A)

# 要素の差が最大になる配列を宣言
MAX_ARRAY = [0] * N

# N=奇数の場合
if N%2 == 1:
    # 中心
    CENTER = int(len(A)/2-0.5)
    # 両端の中央値
    CENTER_VALUE = ( max(A) - min(A) )/2
    # 真ん中の配列の値
    MIDDLE_ARRAY = A[CENTER]

    # 配列の真ん中の値が 配列の中央値よりも小さい場合
    if MIDDLE_ARRAY < CENTER_VALUE:
    
        # 小さめの値を道連れにして両端になる
        MAX_ARRAY[0] = MIDDLE_ARRAY
        MAX_ARRAY[N-1] = A[int(len(A)/2-0.5) -1]

        # 中心は最大値が入る
        MAX_ARRAY[CENTER] = max(A)

        # 残りは中心に行ったやつに近いものを２つ、逆側のやつ２つ、を順に端に詰めてく
        for j in range(N):
            if j==N or j==CENTER or j==CENTER-1:
                psss
            else:
                MAX_ARRAY[j] = A[N-j]
                


        


print (MAX_ARRAY)


