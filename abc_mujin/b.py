a = int(input())
s = str(input())

flag="No"
if a==0:
    flag="Yes"
for i in range(len(s)):
    #print(i)
    if s[i]=="+":
        a+=1
    else:
        a-=1
    if a==0:
        flag="Yes"

print(flag)
