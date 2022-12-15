
for x in range (int(input())):
    s= input()
    cnt,i=1,0
    result=""
    while i<len(s):
        if i<len(s)-1 and s[i]==s[i+1]:
            cnt+=1
        else:
            result += str(cnt)+s[i]
            cnt=1
        i+=1
    print(result)