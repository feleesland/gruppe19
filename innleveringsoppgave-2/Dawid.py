# Dawid sin del av oppgaven. # 

########################################### Konfliktløsning intro Test #########################################
print("\n=== Simulator test for nye prosjektledere TEST #1 ===\n")
print("Velkommen til Konflikt løsning simolator!.\n")
print("I denne simolatoren skal du løse en konflikt mellom to parter, som en prosjekt leder.")
print("Du får flere tre valg å velge mellom, som vil gi deg poeng. Noen handlinger er dårlige, neutrale eller gode.")


print("\nMålet er å løse konflikten på best mulig måte, slik at begge parter blir fornøyde, eller hvor konflikten blir avgjort\n")
print("Du vil få poeng basert på dine valg, og disse poengene vil avgjøre hvor vellykket du er som prosjekt leder.")

############################## Kode for å velge mellom ja eller nei til å starte ##############################
import sys
valg = ""
while valg not in ["ja", "nei"]:
    valg = input ("Er du klar? (ja / nei): ").strip().lower()

    if valg == "ja":
        print("La oss starte simulatoren. Lykke til!")
    elif valg == "nei":
        print("Testen annulert, Lykke til nestegang!\n")
        sys.exit()
    else:
        print("Ugyldig valg, skriv 'ja' eller 'nei'.")

################################################## Start konflikt 1 ###############################################
import random
poeng = 0

print("\nStart av konflikten\n")
print("To teammedlemmer, Silje og Sivert, har en konflikt om arbeidsfordelingen i prosjektet.")
print("Silje føler at hun gjør mer enn sin rettferdige andel av arbeidet, mens Sivert mener at han bidrar like mye.\n")

print("\n=== Hvordan vil du som prosjektleder håndtere denne situasjonen? ====\n")
print("1. La dem diskutere konflikten seg imellom uten din inngripen.")
print("2. Kall dem inn til et møte for å diskutere problemet og finne en løsning sammen.")
print("3. Tildel spesifikke oppgaver til hver av dem uten å involvere dem i beslutningen.")


valg = input("\nSkriv inn ditt valg (1, 2 eller 3):\n")

# Valg 1
if valg == "1":                # Håndterer 50/50 sjanse med tilfeldig utfall
    roll = random.randint(0, 100)
    if roll <= 49:                          # Godt utfall
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


################################################## Start konflikt 2 ###############################################
print("\n ================================ Konflikt 2  ====================================\n")
print(f"Poeng tall: {poeng}\n")

print("\nSelv om konflikten fra i går ble avgjort, så har det ført til en ny krangel\n")

print("\n=== Hvordan vil du som prosjektleder håndtere denne situasjonen? ====\n")
print("1. Du fortalte ledelsen at situasjonen kan ikke bli fikset gjennom din egen involvering.")
print("2. Foreslå en dialogmøte mellom de to partene.")
print("3. Du valgte å ta parti med den ene personen i konflikten.")

valg = input("\nHvordan vil du som prosjektleder håndtere denne situasjonen? (1, 2 eller 3)\n")


if valg == "1":
    poeng += 3
    print("\nDu fortalte ledelsen at situasjonen kan ikke bli fikset gjennom din egen involvering.\n")
    print("Ledelsen satte inn en ekstern mekler for å hjelpe med å løse konflikten.\n")
    print("Dette var et godt valg! Ved å involvere en nøytral tredjepart.")
    print("\nKan du bidra til å sikre at begge parter føler seg hørt og at løsningen er rettferdig.\n")
    print("Som prosjektleder, husk at det å søke ekstern hjelp kan være en effektiv måte å håndtere komplekse konflikter på.\n")

elif valg == "2":
    print("\nForeslå en dialogmøte mellom de to partene.\n")
    poeng += 2
    print("Dette førte til en konstruktiv samtale hvor begge parter følte seg hørt, og de kom frem til en rettferdig arbeidsfordeling.\n")
    print("Dette var et okey valg! Ved å involvere begge parter i samtalen.")
    print("Skaper du en følelse av samarbeid og felles ansvar for løsningen, men det kan hende at underliggende problemer ikke blir fullt ut adressert.\n")

elif valg == "3":
    poeng += 0
    print("\n Du valgte å ta parti med den ene personen i konflikten.\n")
    print("Dette førte til at den andre parten følte seg oversett og undervurdert, noe som eskalerte konflikten ytterligere.\n")
    print("Dette var et dårlig valg! Som prosjektleder er det viktig å være nøytral og rettferdig i konfliktløsning.")
    print("Ved å ta parti kan du skade tilliten og moralen i teamet, noe som kan føre til langvarige problemer.")


################################################## Start konflikt 3 ###############################################
print("\n ================================ Konflikt 3  ====================================\n")
print(f"Poeng tall: {poeng}\n")
print("\nTil tross for dine tidligere forsøk på å løse konflikten, har Silje og Sivert fortsatt problemer med å samarbeide effektivt.\n")
print("\nProsjektets deadline nærmer seg, og dere har en dag igjen til å fullføre oppgaven\n")
print("\nMange stresser, prosjektet er ikke enda klart, og det er et stopp set sted i samerbeidet\n")

print("\n=== Hvordan vil du som prosjektleder håndtere denne situasjonen? ====\n")

print("1. Tving dem til å jobbe sammen for å møte fristen, uansett deres konflikter.")
print("2. Gi dem separate oppgaver som de kan jobbe på individuelt for å møte fristen.")
print("3. Utsett fristen for prosjektet for å gi dem tid til å løse sine konflikter.")
print("4. Lag et møte hvor du prøver å bygge opp motivasjonen og fortelle dem alt de trenger å høre så det minsker stress")
valg = input("\nHvordan vil du som prosjektleder håndtere denne situasjonen? (1, 2, 3 eller 4)\n")

if valg == "1":
    poeng += 0
    print("\nDu valgte å tvinge dem til å jobbe sammen for å møte fristen, uansett deres konflikter.\n")
    print("Dette førte til at samarbeidet deres ble enda mer anstrengt, og kvaliteten på arbeidet deres ble påvirket negativt.\n")
    print("Dette var et dårlig valg! Som prosjektleder er det viktig å vurdere teamets dynamikk og finne måter å fremme samarbeid på.")
    print("Tvang kan føre til motstand og redusert produktivitet.")
elif valg == "2":
    poeng += 2
    print("\nDu valgte å gi dem separate oppgaver som de kan jobbe på individuelt for å møte fristen.\n")
    print("Dette tillot dem å fokusere på sine egne oppgaver uten å måtte håndtere konfliktene direkte, noe som hjalp dem med å møte fristen.\n")
    print("Dette var et okey valg! Ved å gi dem muligheten til å jobbe individuelt, kan du redusere spenningen og hjelpe dem med å fokusere på arbeidet.\n")
elif valg == "3":
    poeng += 1
    print("\nDu valgte å utsette fristen for prosjektet for å gi dem tid til å løse sine konflikter.\n")
    print("Dette ga dem tid til å jobbe gjennom sine problemer, men det skapte også stress for resten av teamet som måtte tilpasse seg den nye tidsplanen.\n")
    print("Dette var et nøytralt valg! Som prosjektleder er det viktig å balansere behovet for å møte frister med behovet for et sunt arbeidsmiljø.\n")
elif valg == "4":
    poeng += 3
    print("\nDu valgte å lage et møte hvor du prøver å bygge opp motivasjonen og fortelle dem alt de trenger å høre så det minsker stress\n")
    print("Dette førte til at begge parter følte seg støttet og motivert til å jobbe sammen for å møte fristen.\n")
    print("Dette var et godt valg! Som prosjektleder er det viktig å anerkjenne teamets følelser og behov.")
    print("Ved å bygge opp motivasjonen kan du bidra til å skape et positivt arbeidsmiljø og fremme samarbeid.")  

################################################## Avslutning ###############################################
print("\n ================================ Avslutning  ====================================\n")
print(f"\nDine totale poeng er: {poeng}\n")
if poeng >= 8:
    print("Gratulerer! Du har vist deg å være en dyktig prosjektleder som kan håndtere konflikter effektivt.")
    print("Dine valg har bidratt til å skape et positivt arbeidsmiljø og fremme samarbeid i teamet.")
elif 5 <= poeng < 8:
    print("Du har gjort en god jobb som prosjektleder, men det er rom for forbedring.")
    print("Vurder hvordan du kan håndtere konflikter mer effektivt i fremtiden for å skape et enda bedre arbeidsmiljø.")
else:
    print("Det ser ut til at du har hatt noen utfordringer som prosjektleder når det gjelder konfliktløsning.")
    print("Vurder å lære mer om effektive konfliktløsningsstrategier for å forbedre dine ferdigheter i fremtiden.")
    
    print("\nTakk for at du deltok i Konflikt løsning simulatoren!")
    print("Lykke til videre med dine prosjektleder ferdigheter.")
    exit()