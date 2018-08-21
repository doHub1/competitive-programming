import re
a, b = map(str, input().split())
s = str(input())


postCode = re.match('[0-9]{'+a+'}-[0-9]{'+b+'}' , s)

if postCode:
  print("Yes")
else:
  print("No")



