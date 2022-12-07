def Xy_Ly_Chuoi(s):
    s.strip()
    while '  ' in s:
        s = s.replace('  ',' ')
    return s.split(',')

s1 = open('Ex86/Ten.inp', 'r').read()
s2 = open('Ex86/QuocTich.inp', 'r').read()

result = zip(Xy_Ly_Chuoi(s1), Xy_Ly_Chuoi(s2))

print(*result)