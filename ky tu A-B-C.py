def check(s):
    return s.count('A')!=0 and s.count('A') <= s.count('B') and s.count('B') <= s.count('C')

def Try(n,s):
    if len(s) == n and check(s):
        print(s)
        return
    elif len(s) == n and check(s) == False: return
    else:
        Try(n,s+'A')
        Try(n,s+'B')
        Try(n,s+'C')

n = int(input())
for i in range(3,n+1):
    Try(i,'')
