
lst = []
for i in range(int(input())):
    s = input()
    # chu de dau, khoang trong, chu de sau khoang trong
    if i == 0 or len(s) == 0 or len(lst[-2]) == 0:
        lst += [s, 0]
    else:
        lst[-1] += 1  # tang cau hoi chu de dang xet
        
for i in range(0, len(lst)-1, 2):
    if (len(lst[i])) > 0:  # neu co chu de
        print(lst[i] + ":", lst[i+1])
