"""[LEARNING LOGS] Colors"""
a = input().capitalize()
b = input().capitalize()

if (a,b) == ("Red","Yellow") or (b,a) == ("Red","Yellow") :
    print("Orange")
elif (a,b) == ("Red","Blue") or (b,a) == ("Red","Blue") :
    print("Violet")
elif (a,b) == ("Yellow","Blue") or (b,a) == ("Yellow","Blue") :
    print("Green")
elif (a,b) == ("Red","Red") :
    print("Red")
elif (a,b) == ("Yellow","Yellow") :
    print("Yellow")
elif (a,b) == ("Blue","Blue") :
    print("Blue")
else :
    print("Error")
