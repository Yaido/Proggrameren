start = 0 

while True:
    tafel = input("Welke tafel wil je dat ik bereken? ")
    if tafel == 1:
        print(start)
        start = start + 1
        if start == 50:
            break

