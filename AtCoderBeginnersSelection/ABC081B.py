# N個のスペース区切りの数値を取得
N = int(input())
A = [int(N) for N in input().split()]

# print (A)
flag = True
ans = 0
while flag:
    # 左端の値から順番にチェック
    for i in range(N):
        # Aが偶数だったらフラグ++してAの値を2で割る
        if A[i] %2 == 0:
            A[i] = A[i] / 2
        # 奇数だったら処理を終了
        else:
            flag = False
            break
    # 全桁に対して2で割ることができたら試行回数（答え）をインクリ
    if flag:
        ans = ans + 1

print(ans)