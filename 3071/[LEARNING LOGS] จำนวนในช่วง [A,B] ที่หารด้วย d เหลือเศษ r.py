"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
A = int(input())
B = int(input())
d = int(input())
r = int(input())
N = 0

for i in range (A , B + 1) :
    if i % d == r :
        N += 1
    i += 1
print(N)
