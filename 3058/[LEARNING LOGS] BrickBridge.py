"""[LEARNING LOGS] BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
b_use = goal // 5
a_use = goal - (b_use * 5)

if b >= b_use and a >= a_use :
    print(a_use)
elif b < b_use and a > goal - (b * 5) :
    print(goal - (b * 5))
else :
    print(-1)
