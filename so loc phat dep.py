
def sodep(n):
    if len(set(n))>2: return "NO"
    for c in s:
        if c!="6" and c!="8": return "NO"
    #xoa cac so dep
    n=n.replace("688", "")
    n=n.replace("68", "")
    n=n.replace("6", "")
    if len(n)>0: return "NO"
    else: return "YES"
s=input()
print(sodep(s))