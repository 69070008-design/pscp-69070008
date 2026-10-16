"""[LEARNING LOGS] Giraffe"""
n = int(input())
giraffe_list = [0]
tall = []

for _ in range(n) :
    h = int(input())
    giraffe_list.append(h)

giraffe_list.append(0)

for i in range(1, n+2) :
    if giraffe_list[i] > giraffe_list[i-1] and giraffe_list[i] > giraffe_list[i+1] :
        tall.append(giraffe_list[i])

print(len(tall))
