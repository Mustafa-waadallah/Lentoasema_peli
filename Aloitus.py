
#Pelin aloitus
aloitus = input("Oletko aikaisemmin pelannut meidän pelin? vasta joo tai ei: ")
print("Tervetuloa lentoasema pelissä")

#ensimmäinen kertaa pelaajalla
username = []
password = []

if aloitus == "ei":
    username1 = input("Anna uusi käyttäjätunnus: ")
    password1 = input("Anna uusi salasana: ")

username.append(username1)
password.append(password1)

#Kirjautuminen

print("Tervetuloa kirjautumaan!")

username2 = input("Kirjoita käyttäjätunnuksesi: ")
if username2 in username:
    password2 = input("Kirjoita salasana: ")

elif username2 not in username:
    print ("Käyttäjätunnus on väärin yritä uudelleen")

if password2 in password:
    print ("Tervetuloa peliin")