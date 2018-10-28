# 一つの文字列の入力
sub = str(input())
key = str(input())
p = []
plane = ''


for i in range(len(sub)):
#    print(ord(s[i]))
    s = ord(sub[i])
    k = ord(key[i])

    if k <= s:
        p.append( s - k +97 )
    else:
        p.append( s - k +26 +97 )
    plane = plane + chr(p[i])

    
print(plane)





