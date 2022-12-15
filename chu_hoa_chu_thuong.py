
s= input()
dem1, dem2= 0, 0

for x in s:
    if x.isupper():
        dem1+=1
    else: dem2+=1
print(s.upper() if dem1>dem2 else s.lower())