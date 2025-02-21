# Program deur Gerrit Smuts:
#
# +++++++ INSTRUKSIES ++++++++
# Die sakrekenaar moet hardloop op "command line"(CMD)
# Die sakrekenaar moet basiese berekeninge doen bv.(Maal *, Plus +, Deel /, en Minus - )
# Die sakrekenaar moet die uitset kan verwyder
# Elke rekenkundige bewerking moet in 'n funksie wees.
# Maak gebruik van 'n "while" of "do while loop" met 'n "sentinel variable" wat gebruik kan word om die "loop" te exit.
# Gebruik # kommentaar met 'n volledige beskrywing van kode se funksie.
#=============================

# Welkomskerm en 'n paar veranderlikes.
print("====WELKOM BY MY SAKREKENAAR====")

# Ek sou aanvanklik hierdie veranderlikes gebruik. Sien kommentaar onder "Opsies waarvan die gebruiker kan kies."
# sentinelExit = "e"
# sentinelDelete = "d"

# Hierdie veranderlike is ingesit om later te gebruik.
verlaat = ""

# Opsies waarvan die gebruiker kan kies:
def opsies():
    print("1 --> Plus +")
    print("2 --> Minus -")
    print("3 --> Maal *")
    print("4 --> Deel /")
    # Die volgende is uitgecomment omdat dit die program te ingewikkeld sou maak.
    # print("5 --> \'n Nommer")
    # print("d --> Vee uit")
    # print("e --> Gaan terug/Kies \'n ander opsie")
    print("v --> Verlaat")
    print("========================================")
    kies = input("Keuse: ")
    return kies

# BEREKENINGE:
# Plus
def plus(x, y):
    return x + y

# Minus
def minus(x, y):
    return x - y

#Maal
def maal(x, y):
    return x * y

# Deel
def deel(x, y):
    return x / y

# Program
while verlaat != "n":
    keuse = opsies()
    if keuse in ("1", "2", "3", "4"):
        try:
            # Gebruiker gee twee nommers.
            nommer1 = float(input("Kies \'n nommer: "))
            nommer2 = float(input("Kies nog \'n nommer: "))
        # As daar iets fout gaan:
        except ValueError:
            print("!KEUSE IS NIE GELDIG NIE! Kies asseblief weer.")
            continue
        # Uitset ná berekeninge
        if keuse == "1":
            print(f"{nommer1} + {nommer2} = {plus(nommer1, nommer2)}")
        elif keuse == "2":
            print(f"{nommer1} - {nommer2} = {minus(nommer1, nommer2)}")
        elif keuse == "3":
            print(f"{nommer1} * {nommer2} = {maal(nommer1, nommer2)}")
        elif keuse == "4":
            print(f"{nommer1} / {nommer2} = {deel(nommer1, nommer2)}")

        # Om die program te verlaat.
        verlaat = input("Wil u aangaan? (ja/nee): ")
        if verlaat == "n" or verlaat == "nee" or verlaat == "Nee":
            verlaat = "n"
        elif verlaat == "j" or verlaat == "ja" or verlaat == "Ja" or verlaat == "y":
            print("========================================")
    elif keuse == "v":
        break
    else:
        print("Keuse nie toegelaat nie. Probeer weer.")