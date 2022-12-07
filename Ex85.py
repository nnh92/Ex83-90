def Get_Max(s):
    Max_Val = max(s)
    Cou_Val = s.count(Max_Val)
    lst = [i for i in range(len(s)) if s[i] == Max_Val]
    return Max_Val, Cou_Val, lst

s = list(input('Nhap day so s: ').split())

lst = Get_Max(s)[2]

print(*lst)