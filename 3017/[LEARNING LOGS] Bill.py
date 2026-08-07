"""[LEARNING LOGS] Bill"""
price = float(input())

if price <= 500 :
    SVC = 50
elif price >= 10000 :
    SVC = 1000
else :
    SVC = price * 0.1

print(f"{((price + SVC) + (price + SVC)*0.07):.2f}")
