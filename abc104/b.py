s = str(input())

ans = "AC"

if s[0] != "A":
    ans = "WA"

if 3 <= s.find('C')+1 <= len(s)-1:
    pass
else:
    ans = "WA"

# C が無いときはこっちで弾ける
if s.find('C') != s.rfind('C'):
    ans = "WA"


index_c = s.find('C')
tmp = s.replace("A", "a")

lower_cases = tmp.replace("C", "c")
if lower_cases != s.lower():
    ans = "WA"




print(ans)
