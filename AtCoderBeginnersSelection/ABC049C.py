#ABC049C - 白昼夢 / Daydream


S = str(input())
#S = 'erasedream'

T = S.replace('dream','').replace('dreamer','').replace('erase','').replace('eraser','')

if T == '':
    print('YES')
else:
    print('NO')
