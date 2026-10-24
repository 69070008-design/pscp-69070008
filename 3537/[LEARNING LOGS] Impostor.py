"""FIND IMPOSTOR"""
import json

amongus = {}
dead_li = []
body = ""
impos_die = 0
player = {}

while True :
    player = input()
    if player != "Start" :
        amongus.update(json.loads(player))
    else :
        break

while True :
    body = input()
    if body in amongus and amongus[body] == "Impostor" :
        impos_die += 1
    if body != "End" :
        dead_li.append(body)
    else :
        break

print(list(amongus.values()).count("Impostor") - impos_die, "Impostor Remains")

print("***Alive***")
for key in sorted(amongus.keys()) :
    if key not in dead_li :
        print(f"{key} : {amongus[key]}")

print("***Dead***")
for key in sorted(amongus.keys()) :
    if key in dead_li :
        print(f"{key} : {amongus[key]}")
