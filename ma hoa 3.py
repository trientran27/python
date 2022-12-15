t=int(input())
while(t>0):
    n=input()
    s1=list(n[0:int(len(n)/2):])
    s2=list(n[int(len(n)/2):len(n):])
    sum1=0
    sum2=0
    for i in s1:
        sum1+=ord(i)-65
    for i in s2:
        sum2+=ord(i)-65
    for i in range(len(s1)):
        s1[i]=chr((ord(s1[i])-65+sum1)%26+65)
    for i in range(len(s2)):
        s2[i]=chr((ord(s2[i])-65+sum2)%26+65)
    for i in range(len(s1)):
        s1[i]=chr((ord(s1[i])-65+ord(s2[i])-65)%26+65)
    print("".join(s1))
    t-=1