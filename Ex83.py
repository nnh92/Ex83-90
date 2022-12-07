def Loc_DL(s, n):
    time = n//len(s) + 1
    lst = time*s[:n]
    return ' '.join(lst)

s = list(input('Nhap day so: ').split())

i = int(input('Nhap so tu nhien: '))

print(Loc_DL(s, i))