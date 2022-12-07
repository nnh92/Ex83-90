def Insert_Data(s, n):
    lst = []
    for i in range(0, len(s), n):
        lst.extend(s[i:i+n])
        lst.append('Han')
    lst.pop()

    return lst

s = list(input('Nhap day s: ').split())

n = int(input('Nhap so nguyen duong n: '))

print(Insert_Data(s, n))