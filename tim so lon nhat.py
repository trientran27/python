#chuyen cac ki tu chu sang khoang trong sau do xet cac ky tu so
for i in range(int(input())):
    s= input()
    for x in s:
        if x.isalpha():
            s= s.replace(x, " ")
    
    s= [int(i) for i in s.split()]
    print(int(max(s)))
