# PRVNI PROJECT

TEXTS_GIVEN = ['''
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

# v textu jsou carky a tecky, ktere mi pak delaji bordel v poctech -> odstranuji
text1 = TEXTS_GIVEN[0].replace(',', '').replace('.','')
text2 = TEXTS_GIVEN[1].replace(',', '').replace('.','')
text3 = TEXTS_GIVEN[2].replace(',', '').replace('.','')

# znovu vytvorim LIST
TEXTS = (text1, text2, text3)

print("-"*40)
print("Welcome to the app. Please log in: ")
user = input("USERNAME: ")
password = input("PASSWORD: ")

user_list = ['bob', 'ann', 'mike', 'liz']
password_list = ['123', 'pass123', 'password123', 'pass123']

dictionary = dict(zip(user_list,password_list))

# pokud by to melo skoncit kdyz zada jmeno, helso blbe, tak bych to psala s if (user, password) in dictionary.items():..atd
while (user, password) not in dictionary.items():  # dokud nebudou spravne user a heslo furt bude chtit input
    user = input("USERNAME: ")
    password = input("PASSWORD: ")

print("-"*40)

print('We have 3 texts to be analyzed.')

text_number = 0

while int(text_number) not in range(1,4):       # dokud nezada uzivatel cislo 1,2,3 furt se ho bude ptat
    text_number = input("Enter a number btw. 1 and 3 to select: ")
    while text_number.isalpha() or text_number == "":
        text_number = input("Enter a number btw. 1 and 3 to select: ")

print("-"*40)

# analyza textu
vybrany_text = int(text_number) - 1
splitak = TEXTS[vybrany_text].split()
pocet_istitle = 0
pocet_isupper = 0
pocet_islower = 0
pocet_isnumeric = 0

for slovo in splitak:
    if slovo.istitle():
        pocet_istitle += 1
    if slovo.isupper():
        pocet_isupper += 1
    if slovo.islower():
        pocet_islower += 1
    if slovo.isnumeric():
        pocet_isnumeric += 1

print("There are",len(splitak),"words in the selected text.")
print("There are", pocet_istitle, "titlecase words.")
print("There are", pocet_isupper,"uppercase words.")
print("There are", pocet_islower,"lowercase words.")
print("There are", pocet_isnumeric,"numeric strings.")
print("-"*40)

text_counter = dict()
pocet_pismen = 0

for slovo in splitak:
    pocet_pismen = len(slovo)
    if pocet_pismen in text_counter.keys():
        text_counter[pocet_pismen] += 1
    else:
        text_counter[pocet_pismen] = 1

klice = list(text_counter.keys())
hodnoty = list(text_counter.values())
delka = len(text_counter)

i = 0

while i < delka:
    print(klice[i],"*"* int(hodnoty[i]), hodnoty[i])
    i += 1

print("-"*40)

import math

suma = 0
for slovo in splitak:
    if slovo.isnumeric():
        suma = suma + float(slovo)

print("If we summed all the numbers in this text we would get: ", suma)
print("-"*40)