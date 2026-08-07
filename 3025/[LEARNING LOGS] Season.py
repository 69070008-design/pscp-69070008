"""[LEARNING LOGS] Season"""
m = int(input())
d = int(input())

if (m in (1,2)) or (m == 3 and d < 21) or (m == 12 and d >= 21) :
    print("winter")
elif (m in (4,5)) or (m == 6 and d < 21) or (m == 3 and d >= 21) :
    print("spring")
elif (m in (7,8)) or (m == 9 and d < 21) or (m == 6 and d >= 21) :
    print("summer")
elif (m in (10,11)) or (m == 12 and d < 21) or (m == 9 and d >= 21) :
    print("fall")
