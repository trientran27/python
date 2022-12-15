
def kt(s):
    if len(set(s)) < 3:
        return "NO"
    if s[0] > s[1]:
        return "NO"
    ok = 1
    for i in range(1, len(s)-1):
        if s[i-1] < s[i] > s[i+1]:
            ok = 0
        if ok == 1:
            if s[i] >= s[i+1]:
                return "NO"
        else:
            if s[i] <= s[i+1]:
                return "NO"
    return "YES"


for _ in range(int(input())):
    s = input()
    print(kt(s))
