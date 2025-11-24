

print("Det har oppstått en konflikt i gruppen")
print("\nKonflikt 1: Silje og Sivert, \nkonflikt 2: Hamdi og Jabir, \nkonflikt 3: Noa og Hallgeir")

Konflikt = input("\nHvilken konflikt vil du løse først? Skriv 1 for Silje og Sivert, 2 Hamdi og Jabir eller 3 for Noa og Hallgeir: ")

def fikse_konflikt1():
    print("Du har valgt å megle mellom Silje og Sivert.")
    print("Silje og Sivert krangler om arbeidsfordelingen i prosjektet.")
    print("\nAlternativ 1: Del oppgavene rettferdig")
    print("Alternativ 2: Be om hjelp fra en veileder")
    valg = input("Velg et alternativ (1 eller 2): ")
    if valg == "1":
        print("Silje og Sivert deler oppgavene rettferdig og løser konflikten.")
    elif valg == "2":
        print("Silje og Sivert ber om hjelp fra en veileder og løser konflikten.")
    else:
        print("Dette er ikke et alternativ, velg 1 eller 2")

def fikse_konflikt2():
    print("Du har valgt å megle mellom Hamdi og Jabir.")
    print("\nAlternativ 1: Finn et kompromiss")
    print("Alternativ 2: Involver en tredjepart")
    valg2 = input("Velg et alternativ (1 eller 2): ")
    if valg2 == "1":
        print("Hamdi og Jabir finner et kompromiss og løser konflikten.")
    elif valg2 == "2":
        print("Hamdi og Jabir involverer en tredjepart som hjelper dem å løse konflikten.")
    else:
        print("Dette er ikke et alternativ")

def fikse_konflikt3():
    print("Du har valgt å megle mellom Noa og Hallgeir.")
    print("\nAlternativ 1: Lytt til hverandre")
    print("Alternativ 2: Søk profesjonell hjelp")
    valg3 = input("Velg et alternativ (1 eller 2): ")
    if valg3 == "1":
        print("Noa og Hallgeir lytter til hverandre og løser konflikten.")
    elif valg3 == "2":
        print("Noa og Hallgeir søker profesjonell hjelp for å løse konflikten.")
    else:
        print("Dette er ikke et alternativ")

# Fiks av resterende problemer uavhengig av første valg

if Konflikt == "1":
    fikse_konflikt1()
    neste = input("\nVil du gå videre til konflikt 2 eller 3?\n Skriv 2 eller 3: ")
    if neste == "2":
        fikse_konflikt2()
        print("\nNå gjenstår bare konflikt 3.")
        fikse_konflikt3()
        print ("Du har løst alle konfliktene")

    elif neste == "3":
        fikse_konflikt3()
        print("\nNå gjenstår bare konflikt 2.")
        fikse_konflikt2()
        print ("Du har løst alle konfliktene")

    else:
        print("\nDette er ikke et alternativ, velg 2 eller 3.")


elif Konflikt == "2":
    fikse_konflikt2()
    neste = input("\nVil du gå videre til konflikt 1 eller 3?\n Skriv 1 eller 3:")
    if neste == "1":
        fikse_konflikt1()
        print("\nNå gjenstår bare konflikt 3.")
        fikse_konflikt3()
        print ("Du har løst alle konfliktene")

    elif neste == "3":
        fikse_konflikt3()
        print("\nNå gjenstår bare konflikt 1.")
        fikse_konflikt1()
        print ("Du har løst alle konfliktene")

    else:
       print ("\nDette er ikke et alternativ, velg 1 eller 3.")

elif Konflikt == "3":
    fikse_konflikt3()
    neste = input("\nVil du gå videre til konflikt 1 eller 2?\n Skriv 1 eller 2:")
    if neste == "1":
        fikse_konflikt1()
        print("\nNå gjenstår bare konflikt 2.")
        fikse_konflikt2()
        print ("Du har løst alle konfliktene")

    elif neste == "2":
        fikse_konflikt2()
        print("\nNå gjenstår bare konflikt 1.")
        fikse_konflikt1()
        print ("Du har løst alle konfliktene")

    else:
        print("\nDette er ikke et alternativ, velg 1 eller 2.")

else:
    print("\nUgyldig valg. Vennligst start på nytt og velg 1, 2 eller 3.")


