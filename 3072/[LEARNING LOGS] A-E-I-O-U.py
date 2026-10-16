"""[LEARNING LOGS] A-E-I-O-U"""
word = input().casefold()
a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

if a > 0 :
    print(f"a : {a}")
if e > 0 :
    print(f"e : {e}")
if i > 0 :
    print(f"i : {i}")
if o > 0 :
    print(f"o : {o}")
if u > 0 :
    print(f"u : {u}")
