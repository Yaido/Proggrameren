import os

score = 0

while True:
    print("Je score is: " + str(score))
    antwoord = input("Wil je klikken? ")
    if antwoord == "nee":
        print("Je bent game over! Je score was: " + str(score) + " punten")
        score = 0
        break
    elif antwoord == "ja" or antwoord == "j" or antwoord == "":
        score = score + 1
    os.system("cls")
