def nt(n):
    if(n<2): return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

#so co 9 uoc so la so c=a^2*b^2 trong do a b la so nt hoac c=x^8
n=int(input())

t=int((n**0.5)/2)
b=int(n**0.125)
lst=[]

for x in range(3, t+1, 2):#tim cac so nguyen to nho hon can n/2
    if(nt(x)):
        lst.append(x)
ans=len(lst)#cac so trong lst c^2*2^2
if 2**8<=n: ans+=1#th so 2 co tu 2^^0 toi 2^^8 co 9 ưoc

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]**2*lst[j]**2<=n:
            ans+=1
        else: break
    if lst[i]<=b: ans+=1#nhung so co mu 8 nho hon n

print(ans)
