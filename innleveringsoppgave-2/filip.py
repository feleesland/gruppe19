# Definerer endepunktsteksten til å kalles, gjør koden ryddigere senere
def endepunkt1():
    print("\nSakskonflikten er løst, men personkonflikten ulmer, og det er en risiko for fremtidige problemer.")

def endepunkt2():
    print("\nEn balansert tilnærmning har blitt nådd med noe relasjonsbygning og noe fremdrift.\n"
          "Men, denne løsningen avhenger av at teammedlemmene er villige til å lytte til hverandre.")

def endepunkt3():
    print("\nKonfliktene er fullstendig løst og teamet er forsterket, godt på langsikt, men det har kostet tid.")

# Definerer spørsmålene slik at man kan følge flytskjemaet basert på brukerens valg
# Silje & Sivert
def beslutning1():
    valg = int(input(
        "\n"
        "En uenighet om teknologivalg har eskalert fra en saklig konflikt til en personkonflikt mellom Silje og Sivert.\n"
        "Silje mener Siverts løsning begrenser innovasjon, mens Sivert anser Siljes forslag som urealistisk og dyrt.\n"
        "Diskusjonene blir stadig mer følelsesladde, og begge mobiliserer støtte fra sine allierte i teamet.\n"
        "\n"
        "Velg alternativ 1 eller 2 for å løse konflikten.\n"
        "1 - Erling tar beslutningen som et tredjeparti ved å lytte til hver enkeltes argumenter \n"
        "\n"
        "2 - Erling fasiliterer en diskusjon mellom Silje og Sivert slik at de kan komme til et kompromiss.\n"))
    return valg

# Hamdi & Jabir
def beslutning2():
    valg = int(input(
        "\n"
        "Parallelt med Silje-Sivert-konflikten oppstår det spenning mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant) om digital deltakelse.\n"
        "Hamdi vil ha en kontrollert løsning via kommunens plattform, mens Jabir ønsker et mer åpent, dialogbasert system.\n"
        "Med bare tre uker til første prototype er stemningen spent og kommunikasjonen dårlig.\n"
        "Erling innser at hans neste beslutninger kan avgjøre om teamet når norming-fasen eller blir stående fast i konflikten.\n"
        "\n"
        "Velg alternativ 1 eller 2 for å løse konflikten.\n"
        "1 - Få partene til å lytte til hverandre og forstå hverandres perspektiv.\n"
        "\n"
        "2 - Innfør en tydelig strukturert beslutningsprosess med felles kriterier for å sikre rettferdig.\n"))
    return valg

# Motivasjon i teamet
def beslutning3():
    valg = int(input(
        "\n"
        "Teamet står i fare for å miste motivasjonen når konflikter og uenigheter tar over.\n"
        "Det er avgjørende at Erling raskt adresserer spenningene før de undergrave engasjementet.\n"
        "Å gjenopprette trygghet og fokus på felles mål er nødvendig for å holde drivet oppe.\n"
        "Uten tiltak risikerer teamet at frustrasjon erstatter entusiasmen som drev prosjektet i starten.\n"
        "\n"
        "Velg alternativ 1 eller 2 for å løse konflikten.\n"
        "1 - Prioritert relasjonbygning og sosiale aktiviter for å sikre trygghet og tillit blandt teamet.\n"
        "\n"
        "2 - Prioriter fremdrift med å sette små overkommelige milåæler temaet kan jobbe mot.\n"))
    return valg

# Innledningstekst
input(
    "\n"
    "Du tar rollen som teamlederen Erling, og skal velge mellom alternativene for å løse konflikter innad teamet.\n"
    "Input '1' eller '2' som svar\n"
    "Trykk 'ENTER' for å forstette")

# Valgprosess og resultat
valg1 = beslutning1() # Silje & Sivert
if valg1 == 1:
    valg2 = beslutning3() # Motivasjon i teamet
    if valg2 == 2:
        endepunkt1()
    else:
        endepunkt2()
elif valg1 == 2:
    valg2 = beslutning2() # Hamdi & Jabir
    if valg2 == 2:
        endepunkt3() 
    else:
        endepunkt2()
else:
    print("\nDet har oppstått en feil.\nInput kun 1 eller 2.\n")