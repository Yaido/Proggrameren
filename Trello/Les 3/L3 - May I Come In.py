print("Goedenavond hoe oud bent u? ")
leeftijd = int(input())

if leeftijd > 18:
    print("Oke, mag ik uw ID zien? ")
elif leeftijd < 17:
    print("Dan mag je helaas niet naar binnen.")
else:
    print(+ str(leeftijd) + "was geen goed antwoord")

antwoord = input()

if antwoord == "ja":
    print("Top, je mag naar binnen!")
elif antwoord == "nee":
    print("Sorry, maar dan kunt u niet naar binnen")
else:
    print(antwoord + "was geen goed antwoord")
