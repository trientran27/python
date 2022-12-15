def lamtron(n):
    if(len(n)==1): return n
    moc=n[0]+"4"*(len(n)-2)+"5"#so moc 
    #neu n lon hon hoac bang moc thi lm tron len
    if(n>=moc): return str(int(n[0])+1) + "0"*(len(n)-1)
    return n[0] + "0"*(len(n)-1)

t=int(input())
for i in range(t):
    n=input()
    print(lamtron(n))