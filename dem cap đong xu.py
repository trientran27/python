import math


t=int(input())

hang, cot=[0]*t, [0]*t

for i in range(t):
    s=list(input())
    for j in range(t):
        if s[j]=='C':
            hang[i]+=1
            cot[j]+=1
ans=0
for c in hang+cot:#ban chat no la 2 vong for rieng biet
    ans+=math.comb(c, 2)#to hop 2 cua c
print(ans)