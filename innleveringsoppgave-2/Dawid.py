# Dawid sin del av oppgaven. # 

############################## Konfliktløsning intro Test ##############################
print("\n=== Simulator test for nye prosjektledere TEST #1 ===\n")
print("Velkommen til Konflikt løsning simolator!.\n")
print("I denne simolatoren skal du løse en konflikt mellom to parter, som en prosjekt leder.")
print("Du får flere tre valg å velge mellom, som vil gi deg poeng. Noen handlinger er dårlige, neutrale eller gode.")


print("\nMålet er å løse konflikten på best mulig måte, slik at begge parter blir fornøyde, eller hvor konflikten blir avgjort\n")
print("Du vil få poeng basert på dine valg, og disse poengene vil avgjøre hvor vellykket du er som prosjekt leder.")

valg = input ("Er du klar? (ja/nei): ")
if valg.lower() != "ja":
    print("La oss starte simulatoren. Lykke til!")
else: valg.lower() != "nei"
print("Testen annulert, Lykke til nestegang!\n")
exit()

############################## Start konflikt 1 #####################################
poeng = 0
import random

print("\nStart av konflikten\n")
print("To teammedlemmer, Silje og Sivert, har en konflikt om arbeidsfordelingen i prosjektet.")
print("Anna føler at hun gjør mer enn sin rettferdige andel av arbeidet, mens Bob mener at han bidrar like mye.\n")

print("\n=== Hvordan vil du som prosjektleder håndtere denne situasjonen? ====\n")
print("1. La dem diskutere konflikten seg imellom uten din inngripen.")
print("2. Kall dem inn til et møte for å diskutere problemet og finne en løsning sammen.")
print("3. Tildel spesifikke oppgaver til hver av dem uten å involvere dem i beslutningen.\n")


valg = input("Skriv inn ditt valg (1, 2 eller 3): ")

# Valg 1
if valg == "1":                # Håndterer 50/50 sjanse med tilfeldig utfall
    roll = random.randint(1, 100)
    if roll <= 50:                          # Godt utfall
        poeng += 1
        print("\nDu valgte å la dem diskutere seg imellom uten din inngrep.")
        print("Dette førte til at konflikten dempet seg, og de har klart å snakke gjennom sine uenigheter\n")
        print("Som en prosjektleder er det viktig å gi teammedlemmer muligheten til å løse konflikter selvstendig når det er mulig.")
        print("Men husk at dette ikke alltid er den beste løsningen for alle situasjoner.\n")
    else:                                   # Dårlig utfall
        poeng += 0
        print("\nDu valgte å la dem diskutere seg imellom uten din inngrep.\n")
        print("Dette førte til at konflikten eskalerte, og begge parter ble mer frustrerte.")
        print("Som en prosjektleder er det viktig å vurdere situasjonens nøye før man tar en beslutning.")

# Valg 2
elif valg == "2":
    poeng += 3
    print("\nDu valgte å kalle dem inn til et møte for å diskutere problemet og finne en løsning sammen.")
    print("Dette førte til en konstruktiv samtale hvor begge parter følte seg hørt, og de kom frem til en rettferdig arbeidsfordeling.\n")
    print("Dette var et godt valg! Ved å involvere begge parter i samtalen.")
    print("Skaper du en følelse av samarbeid og felles ansvar for løsningen.")
    print("Dette kan bidra til å bygge tillit og forbedre arbeidsforholdet mellom dem på lang sikt.\n")
    print ("\nSom en prosjekt leder, husk at selv om denne løsningen var vellykket, kan nye konflikter oppstå i fremtiden.")

# Valg 3
elif valg == "3":
    poeng += 0
    print("\nDu har valgt å gi spesifikke oppgaver til hver av dem uten å involvere dem i beslutningen eller løs konflikten.")
    print("Dette førte til at konflikten midlertidig ble løst, men begge parter følte seg misfornøyde med arbeidsfordelingen.\n")
    print("Partene kan føle seg oversett og undervurdert, noe som kan føre til lavere moral og produktivitet i teamet.\n")
    print("\nSom prosjektleder er det viktig å balansere behovet for effektivitet med rettferdighet og teamets moral.\n")
    print("Uten deres engasjement kan underliggende problemer forbli uløste, noe som kan føre til større og/eller flere fremtidige konflikter.\n")

    
############################## Konflikt 2 #####################################
print("\n ================================ Konflikt 2 ====================================\n")
print("\n Selv om komnflikten ble avgjort, så har det ført til en ny krangel\n")

valg = input("Hvordan vil du som prosjektleder håndtere denne situasjonen? (1, 2 eller 3)")







# Eksempel (legg dette nederst eller bruk som mal):
#-------------------------------------------------
# import random
#
# # rulletall 1..100
# roll = random.randint(1, 100)
#
# # 50% sjanse: 1..50 = lykkelig, 51..100 = dårlig
# if roll <= 50:
#     # håndter lykkelig utfall her
#     print(f"Eksempel: lykkelig (roll={roll})")
#     poeng += 2  # eksempel på poengendring
# else:
#     # håndter dårlig utfall her
#     print(f"Eksempel: dårlig (roll={roll})")
#     poeng += 0
#
#-------------------------------------------------