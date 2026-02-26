import random
##tuo database kursori
#def asemadb():
    ##satunnainen haku databasesta ja näytä siitä tyyppi ja maa koodi
#def profiilitiedot():
    ##databasesta co budjetti, nimi ja uusi tietueetti jossa on listattuna omistetut asemat
    ##myös uusi
kayttisvalinta=float(input(f"1 Anna vanha tunnuksesi\n 2 Aloita uusi"))
if kayttisvalinta=1:
    ##hae vanhan käyttiksen tiedot ja korvaa profiilitiedot niillä
else:
    ##luo uudet tyhjästä
teko=float(input(f"1 Uusi vuoro\n2 Osta asema\n3 Näytä asemat ja omat rahat\n4 Lopeta"))

while(teko!=4):
    teko=float(input(f"1 Uusi vuoro\n2 Osta asema\n3 Näytä asemat ja omat rahat\n4 Lopeta"))
    if(teko==2):
        ##kutsu asemadb:n kolmesti
        input(f"Valitse yksi Näistä:\n1")
        ##päivitä database
    if(teko==3):
        haun_tulos=##tähän haku dbstä
        print(f""haun_tulos"")
