import mysql.connector
import time

#Pelin idea
print("Pelin idea: Pelissä pelaaja omistaa erilaisia lentoasemia.")
print(" Jokainen lentoasema tuottaa pelaajalle rahaa.")
print("Pelaajan tavoitteena on kerätä yhteensä 1000 euroa voittaakseen pelin.")
print("Jos pelaajan rahat putoavat nollaan, peli päättyy häviöön.")

aloitus = input("Oletko pelannut tätä peliä aiemmin? Vastaa: joo tai ei. ")
while aloitus != "joo" and aloitus != "ei":
    print("Yritä uudelleen, kirjoita joo tai ei")
    aloitus = input("Oletko pelannut tätä peliä aiemmin? Vastaa: joo tai ei. ")

#kirjautuminen

def tallentaminen(username, password):
    yhteys = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2006",
        database="logins"
    )
    kursori = yhteys.cursor()
    kursori.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    yhteys.commit()
    kursori.close()
    yhteys.close()

def kirjautuminen():
    print("Tervetuloa kirjautumaan!")

    yhteys = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2006",
        database="logins"
    )
    kursori = yhteys.cursor()

    while True:
        username2 = input("Kirjoita käyttäjätunnuksesi: ")
        kursori.execute("SELECT password FROM users WHERE username = %s", (username2,))
        tulos = kursori.fetchone()

        if tulos is None:
            print("Käyttäjätunnus on väärin, yritä uudelleen")
            continue

        password2 = input("Kirjoita salasana: ")
        if password2 == tulos[0]:
            print("Tervetuloa peliin!!")
            break
        else:
            print("Salasana on väärin, yritä uudelleen!")

    kursori.close()
    yhteys.close()
#ensimmäinen kertaa pelaajalla

if aloitus == "ei":
    username1 = input("Anna uusi käyttäjätunnus: ")
    password1 = input("Anna uusi salasana: ")
    tallentaminen(username1, password1)
    kirjautuminen()
elif aloitus == "joo":
    kirjautuminen()


#nimimerkki

nimimerkki = []

nimi = input("valitse nimimerkki: ")
nimimerkki.append(nimi)
print ("Hello "+ nimi + "!")

#pelaajan rahaa
raha = 100

print("Kirjoita raha, jotta näet rahasi summan. Kun olet valmis, kirjoita lopeta.")
print("Tämän jälkeen näet seuraavan tiedon:")
print("Sinulla on", raha, "euroa raha")

while True:
    money = input()

    if money == "raha":
        print("Sinulla on", raha, "raha")
    elif money == "lopeta":
        break

#Kauppa

print("Kirjoita kauppa nähdääksesi lentoasemien kauppa")


def kauppa():
    global raha
    pelaajan_lentoasemat = []

    print("Osta lentoasema tai hylkää.")
    print("Kirjoita lentoaseman nimi nähdäksesi hinnan ja muut tiedot.")
    lentoasemat = input("valitse yksi: yksityinen lentoasema,"
                        "sotilaslentoasema, vuoristolentoasema,"
                        "turistilentoasema, älylentoasema: ")

    if lentoasemat == "hylkkä":
        print (nimimerkki, "omistaa", pelaajan_lentoasemat)

#Ensimmäinen lentoasema
    if lentoasemat == "yksityinen lentoasema":
        print("Lentoaseman hinta on 100 euro")
        ostaminen = input("Kirjoita 'osta' ostaaksesi lentoaseman: ")
        if ostaminen == "osta" and raha >= 100:
            print("yksityinen lentoasema on ostettu.")
            raha -= 100
            print("Raha jäljellä: ", raha)
            input("Kirjoita lentoaseman nimi että pystyt raha tienata: ")
            while True:
                time.sleep(1)
                raha += 0.05
                print("Rahasi:", (raha))
                lopeta = input()
                if lopeta == "lopeta":
                    break
        elif raha < 100:
            print("Sinulla ei ole riittävä raha")

#toinen lentoasema
    if lentoasemat == "sotilaslentoasema":
        print("Lentoaseman hinta on 100 euro")
        ostaminen = input("Kirjoita 'osta' ostaaksesi lentoaseman: ")
        if ostaminen == "osta" and raha >= 100:
            print("Sotilas lentoasema on ostettu.")
            raha -= 100
            print("Raha jäljellä: ", raha)
            input("Kirjoita lentoaseman nimi että pystyt raha tienata: ")
            while True:
                time.sleep(1)
                raha += 0.05
                print("Rahasi:", (raha))
                lopeta = input()
                if lopeta == "lopeta":
                    break
        elif raha < 100:
            print("Sinulla ei ole riittävä raha")

#Kolmas lentoasema

    if lentoasemat == "turistilentoasema":
        print("Lentoaseman hinta on 100 euro")
        ostaminen = input("Kirjoita 'osta' ostaaksesi lentoaseman: ")
        if ostaminen == "osta" and raha >= 100:
            print("turistilentoasema on ostettu.")
            raha -= 100
            print("Raha jäljellä: ", raha)
            input("Kirjoita lentoaseman nimi että pystyt raha tienata: ")
            while True:
                time.sleep(1)
                raha += 0.05
                print("Rahasi:", (raha))
                lopeta = input()
                if lopeta == "lopeta":
                    break
        elif raha < 100:
            print("Sinulla ei ole riittävä raha")

#Neljäs lentoasema

    if lentoasemat == "älylentoasema":
        print("Lentoaseman hinta on 100 euro")
        ostaminen = input("Kirjoita 'osta' ostaaksesi lentoaseman: ")
        if ostaminen == "osta" and raha >= 100:
            print("älylentoasema on ostettu.")
            raha -= 100
            print("Raha jäljellä: ", raha)
            input("Kirjoita lentoaseman nimi että pystyt raha tienata: ")
            while True:
                time.sleep(1)
                raha += 0.05
                print("Rahasi:", (raha))
                lopeta = input()
                if lopeta == "lopeta":
                    break
        elif raha < 100:
            print("Sinulla ei ole riittävä raha")

while True:
    lentoasemat = input()
    if lentoasemat == "kauppa":
        kauppa()
        break

#pelaaja kerää rahaa siivouksesta
print("jos rahat eivät riittää tai haluat tienata enemmän, kerää ne siivouksesta.")
print("saat 0.025 euroa sekunnista")
siivous = input("kirjoita siivous sana aloittaaksesi siivous")

if siivous == "siivous":
    print("Siivous alkoi! Kirjoita 'lopeta' lopettaaksesi: ")
    while True:
        time.sleep(1)
        raha += 0.05
        print("Rahasi:", (raha))
        lopeta = input()
        if lopeta == "lopeta":
            break
while True:
    kertominen = input("Kirjoita komento: ")

    if kertominen == "raha":
        print("Sinulla on", raha, "euroa")

    if kertominen == "kauppa":
        kauppa()

    if kertominen == "siivous":
        print("Siivous alkoi!")
        while True:
            time.sleep(1)
            raha += 0.05
            print("Rahasi:", raha)
            if input() == "lopeta":
                break