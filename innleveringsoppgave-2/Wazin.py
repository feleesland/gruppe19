def fikse_konflikt1():
    print("Silje og Sivert har hatt en konflikt fordi Sivert glemte å levere en viktig oppgave som Silje trengte for å fullføre sitt arbeid.")
    print("alternativ1: Sivert kan be om unnskyldning og love å være mer pålitelig i fremtiden.")
    print("alternativ2: Silje kan tilby å hjelpe Sivert med å organisere arbeidet sitt bedre.")
    valg = input("Velg et alternativ (1 eller 2): ")
    if valg == "1":
        
        print("Sivert ber om unnskyldning, og de blir enige om å kommunisere bedre fremover.")
    elif valg == "2":
        
        print("Silje hjelper Sivert, og de finner en løsning sammen.")
    else:
        print("Velg 1 eller 2")


def fikse_konflikt2():
    print("Hamdi og Jabir har hatt en konflikt fordi Hamdi følte at Jabir ikke respekterte hans meninger under gruppemøter.")
    print("alternativ1: Jabir kan lytte mer aktivt og anerkjenne Hamdis synspunkter.")
    print("alternativ2: Hamdi kan uttrykke sine følelser på en rolig måte og be om respekt.")
    valg = input("Velg et alternativ (1 eller 2): ")
    if valg == "1":
        
        print("Jabir lytter mer aktivt, og de finner en felles forståelse.")
    elif valg == "2":    
        print("Hamdi uttrykker sine følelser, og de blir enige om å respektere hverandre.") 
    else:
        print("Velg 1 eller 2")


def fikse_konflikt3():
    print("Noa og Hallgeir har hatt en konflikt fordi Noa følte at Hallgeir tok for mye kontroll over gruppens beslutninger.")
    print("alternativ1: Hallgeir kan gi Noa mer rom til å bidra i beslutningsprosessen.")
    print("alternativ2: Noa kan foreslå en struktur for hvordan beslutninger skal tas i gruppen.")
    valg = input("Velg et alternativ (1 eller 2): ")
    if valg == "1":
        
        print("Hallgeir gir Noa mer rom, og de samarbeider bedre.")
    elif valg == "2":    
        print("Noa foreslår en struktur, og gruppen blir mer organisert.") 
    else:
        print("Velg 1 eller 2")


print("det har oppstått en konflikt i gruppen")
print("\nKonflikt 1: Silje og sivert, \nKonflikt 2: Hamdi og Jabir, \nKonflikt 3: Noa og Hallgeir")

antall_konflikter = 3

while antall_konflikter > 0:
    valgt_konflikt = int(input("Hvilken konflikt ønsker du å løse? (1, 2 eller 3): "))
    if valgt_konflikt == 1:
        fikse_konflikt1()
        antall_konflikter -= 1
    elif valgt_konflikt == 2:
        fikse_konflikt2()
        antall_konflikter -= 1
    elif valgt_konflikt == 3:
        fikse_konflikt3()
        antall_konflikter -= 1
    else:
        print("Velg en gyldig konflikt (1, 2 eller 3).")
