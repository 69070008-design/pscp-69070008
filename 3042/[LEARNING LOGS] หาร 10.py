"""[LEARNING LOGS] หาร 10"""
N = int(input())
n = N // 10
num10x = [0]

for i in range(n) :
    i += 1
    num10x.append(i * 10)
num10x.sort(reverse=True)
print(*num10x)
