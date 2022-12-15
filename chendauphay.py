
s=input()

n=len(s)
result=""
if n%3==1:
    result+=s[0]
    for i in range(1,n, 3):
        result += "," + s[i:i+3]
elif n%3==2:
    result+=s[0:2]
    for i in range(2,n, 3):
        result += "," + s[i:i+3]
else:
    result+=s[0:3]
    for i in range(3,n, 3):
        result += "," + s[i:i+3]
print(result)