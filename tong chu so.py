
n = input()
sum=0
while len(n)>1:
    tong=0
    sum+=1
    if n[0]=="-": tong+=ord("-")-ord("0")
    else: tong+=int(n[0])
    for c in n[1:]:
        tong+=int(c)
    n=str(tong)
print(sum)