# N個のスペース区切りの数値を取得
N = int(input())
A = [int(N) for N in input().split()]


# 奇数番目と偶数番目に出てくる数字の頻度順にそれぞれソートして、
odd = []
even = []

for i in range(N):
    if i%2 == 0:
        odd.append(A[i])
    else:
        even.append(A[i])

import collections
c_odd = collections.Counter(odd)
c_even = collections.Counter(even)
#print(c_odd.most_common()[0][0], c_even.most_common()[0][0])



# 最頻な数字が一致してない場合はそれぞれの最頻値以外の合計値、
if c_odd.most_common()[0][0] != c_even.most_common()[0][0] :
    #print(len(set(odd))-1 + len(set(even))-1)
    print(N - c_odd.most_common()[0][1] - c_even.most_common()[0][1])
    exit()


# 一致してる場合は片方が最頻を諦めた場合の合計値を両パターン求めて小さい方
if c_odd.most_common()[0][0] == c_even.most_common()[0][0] :

    # 偶数と奇数の数列が完全一致のパターンでないかチェック
    if len(c_odd.most_common()) == 1 and len(c_even.most_common()) == 1:
        print(N//2)

    # oddが1種類しかない場合
    elif len(c_odd.most_common()) == 1:
        print(N//2 - c_even.most_common()[1][1])
    # evenが1種類しかない場合
    elif len(c_even.most_common()) == 1:
        print(N//2 - c_odd.most_common()[1][1])
    #両方が2種類以上で構成されている場合
    else:
        ans = N - max(c_odd.most_common()[0][1]+c_even.most_common()[1][1], c_odd.most_common()[1][1]+c_even.most_common()[0][1] )
        print(ans)

'''
        # 最頻を諦める ＝ 2番めに頻出な数値を採用
        temp_odd_retire = N//2 - c_odd.most_common()[1][1] #個数
        temp_even_retire = N//2 - c_even.most_common()[1][1] #個数
        #print('temps are ', temp_odd_retire, temp_even_retire)

        # oddを諦めたほうが良い場合
        if temp_odd_retire < temp_even_retire:
            print(temp_odd_retire + N//2 - c_even.most_common()[0][1])
        # even()
        else:
            print(temp_even_retire + N//2 - c_odd.most_common()[0][1])
        exit()
'''
