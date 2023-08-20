dicx = {"key_1":1,
        3: "val_2",
        "k3":  {"key_nested_1": 3.4,
             "key_nested_2": "salut"}}

print(dicx["k3"]["key_nested_2"])

for key, value in dicx.items():
    #iterez pe chei si valori
    print(f"Pentru cheia {key} avem valoarea {value}")

for una_din_chei in dicx.keys():
    #iterez doar pe chei
    print(f"Cheia {una_din_chei}")

for valoare in dicx.values():
    #iterez doar pe valori
    print(f"Valoarea = {valoare}")

dicx["cheia_5"] = ["nume 1", "nume 2"]
print(dicx)

lisa = ["a", "b", "c"]
lisb = [1, 2, 3]

dictionar_din_liste = dict(zip(lisa, lisb))
print(dictionar_din_liste)

import json

dicx = {"key_1":1,
        3: "val_2",
        "k3":  {"key_nested_1": 3.4,
             "key_nested_2": "salut"}}



print(dicx)
dictionar_frumos = json.dumps(dicx, indent=2)
print(dictionar_frumos)

folder = "B:/pyx/SDA/sda_51"
with open(f"{folder}/exemplu_json.txt", "w") as f:
    json.dump(dicx, f) #dump transforma din dictionar in string

#Citesc fisierul cu dictionar
with open(f"{folder}/exemplu_json.txt", "r") as f:
    datele_mele = json.load(f) #load a transformat din text in dictionar, daca textul este valid

print(datele_mele)
print(type(datele_mele))

stringx = json.dumps(dicx) #dumps transforma un obiect de tip dictionar in tip string
print(stringx, type(stringx))

strx = '{"key_1":1,"3":"val_2","k3":{"key_nested_1": 3.4,"key_nested_2": "salut"}}'

dictionar_din_string = json.loads(strx)
print(dictionar_din_string)
print(type(dictionar_din_string))

#dict & list comprehension
nume_prenume_varsta_tuplu = (("Ionescu", "Ion", 29),
                       ("Vasilescu", "Vasile", 22),
                       ("Ailenei", "Elena", 30),
                       ("Abc", "Ana", 26))

dict_pv = {prenume: varsta for nume, prenume, varsta in nume_prenume_varsta_tuplu}
print(dict_pv)

dict_pv3 = {prenume: varsta + 3 for prenume, varsta in dict_pv.items()}
print(dict_pv3)

dict_cuburi = {nr: nr**3 for nr in range(5, 17)}
print(dict_cuburi)

#List comprehension
lis_1 = [3, 18, 2, 1, 10]
lis_1_3 = [x**3 for x in lis_1]
print(lis_1_3)

#calculez cuburile doar daca numerele sunt pare
lis_1_3_pare = [x**3 for x in lis_1 if x%2==0]
print(lis_1_3_pare)

matrix = [[1,2,3], [11,22,33], [12, 13, 14]]
"""
1 2 3
11 22 33
12 13 14
Vreau sa obtin [1,2,3,11,22,33,12, 13, 14]
"""

flat = [x for row in matrix for x in row]
print(flat)

#V2 desfasurata
flat_v2 = list()
for row in matrix:
    for x in row:
        flat_v2.append(x)

print(flat_v2)

nume = ["iOn", "anA", "eLEna"]
nume_corect = [n.capitalize() for n in nume]
print(nume_corect)

nume = input("Zi numele tau = ")
print(f"Salutare {nume}, incantat de cunostinta")

varsta = input("Ce varsta ai? = ")
print(varsta, type(varsta))

#ca sa verificam daca str este integer valid
if varsta.isdigit():
    print(f"Peste 3 ani vei avea {int(varsta) + 3} ani")
else:
    print("Mai scrie o data varsta valida ca integer")

a1 = 'SAlutare34-'
print(a1.isalpha()) #isalpha verifica daca un string contine doar litere a-Z
print(a1.isalnum()) #isalnum verifica a-Z0-9
a2 = 'saLut'
print(a2.islower()) #islower - verifica daca toate caracterele sunt lowercase
print(a2.isupper()) #isupper- daca sunt UPPERCASE
a3 = """ 

                
"""
print(a3.isspace()) #isspace - daca se contin doar spatii, newline, tabs

def suma(a,b):
    return a+b

print(suma(3,4))

def suma_x(*args):
    suma_totala = 0
    for a in args:
        if str(a).isdigit():
            suma_totala += int(a)
    return suma_totala

print(suma_x(3,"4",5,10))

def nume_varsta(**kwargs):
    print(kwargs)
    for nume, varsta in kwargs.items():
        print(f"{nume} are {varsta} ani")

nume_varsta(Ion=3, Vasile=5, Ana=4, Andrei=3.2, Elena= 4.2)

#Exeritiu de ghicit un numar, cu "Esti departe", "Aproape", "Foarte aproape", "Ai ghicit".
