"""[LEARNING LOGS] SurprisingVote"""
total = float(input())
popvote = float(input())
least = total - popvote*2

if least <= 0 :
    least = 0
different = popvote - least

if 0 <= different <= 2 :
    print("Not surprising")
elif different > 2 :
    print("Surprising")
