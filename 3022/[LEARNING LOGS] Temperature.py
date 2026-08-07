"""[LEARNING LOGS] Temperature"""
temp = float(input())
typ1 = input()
typ2 = input()
c = 0

if typ1 == "C" :
    c = temp
elif typ1 == "K" :
    c = temp - 273.15
elif typ1 == "F" :
    c = ((temp * 5) - 160)/9
elif typ1 == "R" :
    c = (temp * 5/9) - 273.15

"""if typ1 == typ2 :
    print(f"{temp:.2f}")"""
if typ2 == "C" :
    print(f"{c:.2f}")
elif typ2 == "K" :
    print(f"{(c + 273.15):.2f}")
elif typ2 == "F" :
    print(f"{((c * 9/5) + 32):.2f}")
elif typ2 == "R" :
    print(f"{((c + 273.15) * 9/5):.2f}")
