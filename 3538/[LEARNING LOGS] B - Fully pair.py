"""[LEARNING LOGS] B - Fully pair?"""
letter = input()
letter_list = []
letter_single = []

for l in letter :
    if l not in letter_list :
        letter_list.append(l)

for a in letter_list :
    if letter.count(a) % 2 :
        letter_single.append(a)

if not letter_single :
    print("fully paired")
else :
    print("".join(letter_single))
