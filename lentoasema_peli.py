import mysql.connector
import time

#Pelin idea
print("Pelin idea: Pelissä pelaaja omistaa erilaisia lentoasemia.")
print(" Jokainen lentoasema tuottaa pelaajalle rahaa.")
print("Pelaajan tavoitteena on kerätä yhteensä 1000 euroa voittaakseen pelin.")
print("Jos pelaajan rahat putoavat nollaan, peli päättyy häviöön.")

#Pelin aloitus
aloitus = input("Oletko pelannut tätä peliä aiemmin? Vastaa: joo tai ei.")

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
    username = []
    password = []

    username.append(username1)
    password.append(password1)

    username2 = input("Kirjoita käyttäjätunnuksesi: ")
    if username2 in username:
            password2 = input("Kirjoita salasana: ")
    while username2 not in username:
        print ("Käyttäjätunnus on väärin yritä uudelleen")
        username2 = input("Kirjoita käyttäjätunnuksesi: ")
        if username2 in username:
            password2 = input("Kirjoita salasana: ")
            if password2 not in password:
                print("salasna on väärin, yritä uudelleen!")
                password2 = input("Kirjoita salasana: ")
        if username2 in username and password2 in password:
            print("Tervetuloa peliin!!")
            tallentaminen(username2, password2)

#ensimmäinen kertaa pelaajalla

if aloitus == "ei":
    username1 = input("Anna uusi käyttäjätunnus: ")
    password1 = input("Anna uusi salasana: ")
    tallentaminen(username1, password1)
    kirjautuminen()


#nimimerkki

nimimerkki = []

nimi = input("valitse nimimerkki: ")
nimimerkki.append(nimi)
print ("Hello "+ nimi + "!")

#pelaajan rahaa
raha = 50

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

    pelaajan_lentoasemat = []

    print("Osta lentoasema tai hylkää.")
    print("Kirjoita lentoaseman nimi nähdäksesi hinnan ja muut tiedot.")
    lentoasemat = input("valitse yksi: yksityinen lentoasema,"
                        "sotilaslentoasema, vuoristolentoasema,"
                        "turistilentoasema, älylentoasema: ")

    if lentoasemat == "hylkkä":
        print (nimimerkki, "omistaa", pelaajan_lentoasemat)

    if lentoasemat == "yksityinen lentoasema":
        print("Lentoaseman hinta on 100 euro")

    if lentoasemat == "sotilaslentoasema":
        print("Lentoaseman hinta on 100 euro")

    if lentoasemat == "turistilentoasema":
        print("Lentoaseman hinta on 100 euro")

    if lentoasemat == "älylentoasema":
        print("Lentoaseman hinta on 100 euro")

while True:
    lentoasemat = input()
    if lentoasemat == "kauppa":
        kauppa()
        break


#pelaaja kerää rahaa siivouksesta
print("jos rahat eivät riittää, kerää ne siivouksesta.")
print("saat 0.025 euroa sekunnista")
siivous = input("kirjoita siivuos sana aloittaaksesi siivous")

if siivous == "siivous":
    print("Siivous alkoi! Kirjoita 'lopeta' lopettaaksesi.")
    while True:
        time.sleep(1)
        raha += 0.025
        print("Rahasi:", (raha))
        if siivous == "lopeta":
            break