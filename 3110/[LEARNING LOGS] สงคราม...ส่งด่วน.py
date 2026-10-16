"""[LEARNING LOGS] สงคราม...ส่งด่วน"""
lo_tag = input()
weight = float(input())
fee = 0
ship_p = 0

if lo_tag == "BKK CNX" :
    fee = 10
    ship_p = 30
elif lo_tag == "CNX UBP" :
    fee = 15
    ship_p = 40
elif lo_tag == "UBP BKK" :
    fee = 20
    ship_p = 40
elif lo_tag == "BKK PKT" :
    fee = 25
    ship_p = 50
elif lo_tag == "PKT CNX" :
    fee = 30
    ship_p = 60
elif lo_tag == "UBP PKT" :
    fee = 40
    ship_p = 70

if not fee :
    print("Error")
else :
    print(f"{fee + (weight * ship_p) :.2f}")
