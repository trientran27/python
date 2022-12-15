import re

s=""
while True:
    try:
        s+=input()
    except EOFError:
        break
s=re.split('[.?!]', s)#cat cac cau
for x in s:
    if len(x)>0:
        c=re.sub('\s+', ' ', x.strip())#cat cac khoang trang thua, khoang trang 2 dau
        print(c[0].upper() + c[1:].lower())
 