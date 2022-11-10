print("Ga je naar school met de fiets of met OV?")
antwoord = input()

if antwoord == ("ov"):
    print("Je bent te moe om zo vroeg al te fietsen")
elif antwoord == ("fiets"):
    print("Je bent lekker fit en gaat met de fiets")
else:
    print( + str(antwoord) + "was niet goed")

print("Volg je liever online les of ga je liever naar school toe?")
keuze = input()

if keuze == ("online"):
    print("Je volgt liever online les omdat je dan langer in je bed kan liggen.")
elif keuze == ("school"):
    print("Je kan je thuis niet zo goed concentreren.")
else:
    print( + str(keuze) + "was niet goed")

print("Sta je meestal vroeg of laat op?")
antwoord = input()

if antwoord == ("vroeg"):
    print("Je bent altijd vroeg wakker")
elif antwoord == ("laat"):
    print("Je bent een slaapkop")
else:
    print( + str(antwoord) + "was niet goed")

print("Vind jij voetballen leuker of binnen zitten")
antwoord = input()

if antwoord == ("voetballen"):
    print("Je bent lekker fit.")
elif antwoord == ("binnen zitten"):
    print("Je bent saai.")
else:
    print( + str(antwoord) + "was niet goed")

print("Vind je apple of android beter?")
antwoord = input()

if antwoord == ("apple"):
    print("Je bent apple gewend.")
elif antwoord == ("android"):
    print("Je bent android gewend.")
else:
    print( + str(antwoord) + "was niet goed")