#!/usr/bin/python
# coding: UTF-8
import math, string
# 10進数整数を2進数文字列に変換する関数
# decimal : 10進数整数
# press   : 上位桁の0を切り詰めるフラグ
def toBinary(decimal, press=True):
    if decimal == 0: return '0'
    bin_str = ""
    i = 31
    while i >= 0:
        bi = int((decimal & int(math.pow(2, i))) >> i)
        bin_str += str(bi)
        i -= 1
    if press:
        try:
            bin_str = bin_str[bin_str.index('1'):]
        except ValueError:
            print 'error'
            bin_str = '0'
    return bin_str
bin_arr = [toBinary(i) for i in range(21)]
print('10進数t2進数')
for i in range(len(bin_arr)):
    print('%2dt%5s' % (i, bin_arr[i]) )

