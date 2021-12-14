"""
author = František Kalánek
"""
from typing import Dict, Any

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

# uzivatele
uzivatel = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    "liz": "pass123"
}

oddelovac = "-" * 40

# 1.Vyžádá si od uživatele přihlašovací jméno a heslo.

jmeno = input("username:")
heslo = input("password:")
print(oddelovac)

# 2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
if uzivatel.get(jmeno) == heslo:
    print("Welcome to the app,", jmeno)
else:
    print("Wrong name or password")
    quit()
print("We have 3 texts to be analyzed.")
print(oddelovac)

# Program nechá uživatel vybrat mezi třemi texty
vyber = input("Enter a number btw. 1 and 3 to select:")
if vyber.isalpha():
    print("Selection is not a number")
    quit()

else:
    vyber = int(vyber)

if vyber <= 3 and vyber >= 1:
    print(oddelovac)
else:
    print("Number is not btw 1-3")
    quit()

upraveny_vyber = TEXTS[vyber - 1]

# Pro vybraný text spočítá následující statistiky:

# počet slov
vycisteny_text = list()
for slovo in upraveny_vyber.split():
    vycisteny_text.append(slovo.strip(",.:;"" "))

for word in vycisteny_text:
    if word == "":
        vycisteny_text.remove(word)
#print(vycisteny_text)

print("There are", len(vycisteny_text), "words in the selected text")

# - počet slov začínajících velkým písmenem
velke = []

for slovo in vycisteny_text:
    if slovo[0].isupper():
        velke.append(slovo[0])

print("There are", len(velke), "titlecase words.")

# - počet slov psaných velkými písmeny,
velka = []
for slova in vycisteny_text:
    if slova.isupper() and slova.isalpha():
        velka.append(slova)

print("There are", len(velka), "uppercase words.")

# - počet slov psaných malými písmeny,
mala = []
for i in vycisteny_text:
    if i.islower() and i.isalpha():
        mala.append(i)

print("There are", len(mala), "lowercase words.")

# počet čísel (ne cifer)
cisla = []
for x in vycisteny_text:
    if x.isnumeric():
        cisla.append(x)

print("There are", len(cisla), "numeric strings.")

# sumu všech čísel (ne cifer) v textu.

suma = list(map(int, cisla))
print("The suma of all the numbers:", sum(suma))

print(oddelovac)

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu

print("LEN|  OCCURENCES  |NR.")
print(oddelovac)

#print(vycisteny_text)

#spocitat vyskyt pro kazde slovo

delka_slov = dict()
for slovo in vycisteny_text:
    # pokud delka slova neni ve slovniku, vytovri se jeji key s hodnotou nula
    if len(slovo) not in delka_slov:
        delka_slov.setdefault(len(slovo), 0)
    else:
    # prictu jednicku ke spravne delce slova v dictionary
        delka_slov[len(slovo)] = delka_slov[len(slovo)] + 1

#print(delka_slov)

hvezda = "*"

list_delek = []
for slovo in vycisteny_text:
    list_delek.append(len(slovo))
#print(list_delek)

serazene = sorted(list_delek, reverse=False)[::]
#print("serazene", serazene)

dict_delek = {}
for delka in serazene:
   if delka in dict_delek:
        dict_delek[delka] += 1
   else:
        dict_delek[delka] = 1

#print((dict_delek))

# Slova s nejcastesjim vyskytem
for x, y in dict_delek.items():
    print(f"{x}  |{(hvezda) * (y):<13} |{y}")




