#--------------Konfliktløsning på Jobb-----------------
print("\n=== KONFLIKTLØSNING PÅ JOBB ===\n")
print("Du er ny prosjektleder. To kolleger, Silje og Sivert, er i konflikt.\n")

konstruktiv = 0

# --- LEDD 1 ---
print("LEDD 1 - Første tegn på konflikt")
print("Under et møte merker du at tonen mellom Silje og Sivert er passiv-aggressiv.")
print("Hva gjør du?")
print("1: Tar prat med begge etter møtet.")
print("2: Ignorerer situasjonen og håper det løser seg selv.")
choice1 = input("Valg (1/2): ")

if choice1 == "1":
    konstruktiv += 1
    print("Du velger å snakke med dem hver for seg for å forstå situasjonen.\n")
else:
    print("Du velger å ignorere situasjonen for nå.\n")

# --- LEDD 2 ---
print("LEDD 2 - Konflikten eskalerer")
print("En uke senere eskalerer konflikten i et møte.")
print("Hva gjør du?")
print("1: Foreslår et dialogmøte.")
print("2: Informerer sjefen og overlater håndteringen til ledelsen lengre opppe.")
choice2 = input("Valg (1/2): ")

if choice2 == "1":
    konstruktiv += 1
    print("Du legger opp til et dialogmøte.\n")
else:
    print("Du overlater det til ledelsen å ta tak i saken.\n")

# --- LEDD 3 ---
print("LEDD 3 - Et mulig vendepunkt")
print("Prosjektet nærmer seg deadline, og teamet kjenner konflikten.")
print("Hva gjør du?")
print("1: Setter klare samarbeidsregler og leder ukentlige check-ins.")
print("2: Fordeler oppgaver slik at de slipper å samarbeide direkte.")
choice3 = input("Valg (1/2): ")

if choice3 == "1":
    konstruktiv += 1
    print("Du legger til rette for bedre kommunikasjon.\n")
else:
    print("Du skiller dem i arbeidet for å unngå mer konflikt.\n")

# --- AVGJØRELSE ---
print("\n=== SLUTTRESULTAT ===")

if konstruktiv >= 2:
    print("\nAVSLUTNING 1 - Konstruktiv suksess")
    print("Silje og Sivert får snakket ordentlig sammen og samarbeidet styrkes.")
    print("Prosjektet fullføres med god stemning.")
elif konstruktiv == 1:
    print("\nAVSLUTNING 2 - Midlertidig løsning")
    print("Konflikten roer seg nok til at prosjektet blir ferdig, men det er fortsatt spenning i laget.")
    print("Du gjorde mye bra, men du hadde valg som kunne ha ført til et bedre resultat.")
else:
    print("\nAVSLUTNING 3 - Konflikten fryses, men den har ikke blitt løst")
    print("Prosjektet blir ferdig, men samarbeidet har blit værre.")
    print("Du innser at konflikter sjelden løser seg selv")

print("\nLykke til med videre beslutninger!\n")
