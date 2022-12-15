n, m=[int(x) for x in input().split()]

lst, max=[], 0
for i in range(n):
    s=input().split()
    for j in range(len(s)):
        if int(s[j])>max and int(s[j])>10 and s[j]==s[j][::-1]:
            max=int(s[j])
            lst =["[" + str(i)+"]" + "[" + str(j)+"]"]
        elif int(s[j]) == max:
            lst += ["[" + str(i) + "]" + "[" + str(j) + "]"]
if len(lst)==0:
    print("NOT FOUND")
else:
    print(max)
    for x in lst:
        print("Vi tri " + x)