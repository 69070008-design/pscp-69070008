"""[LEARNING LOGS] Duplicate I"""
m = int(input())
n = int(input())

have_group = set()
sus = set()

for _ in range(m+n) :
    ID = int(input())
    if ID in have_group :
        sus.add(ID)
    else :
        have_group.add(ID)

if sus :
    for i in sorted(sus, reverse=True) :
        print(i)
else :
    print("Nope")
