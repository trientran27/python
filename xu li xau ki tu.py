#chuan hoa thanh cac ki tu thuong va loai bo tu trung nhau
a=set(input().lower().split())
b=set(input().lower().split())

c= sorted(a|b)
d= sorted(a&b)
print(" ".join(c))
print(" ".join(d))