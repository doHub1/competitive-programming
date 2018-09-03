import re
before = str(input())
after = re.sub(r"2017","2018",before)
if after:
    print(after)

