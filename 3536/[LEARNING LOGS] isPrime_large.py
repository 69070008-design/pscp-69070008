"""[LEARNING LOGS] isPrime_large"""
n = int(input())
ans = "YES"

for i in range(2,int(n**0.5)+1) :
    if not n % i :
        ans = "NO"
        break

if n == 1 :
    ans = "NO"

print(ans)
