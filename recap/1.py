#tipuri de date
a = 2
print(type(a))
b = 2.3
print(type(b)) #float - rationale
c = 'salut'
d = "Salut"
print(type(c), type(d)) #str = text
e = False
f = True #boolean data type

lis_1 = [1, 2.3, [33, 22], "ceva", False]
print(type(lis_1))
set_2 = {1,2,3,1,1,2}
print(set_2, type(set_2)) #{1, 2, 3} <class 'set'>
tup_1 = (2,3,5.3)
print(type(tup_1))
dict_1 = {"cheie_1": "valoare_1",
          "cheie_2": "valoare_2",
          "cheie_3": {1:2, 3:4.5}}
print(type(dict_1))

print(2+3)
print(2**3)
print(17//5) #impartirea fara rest
print(17%5) #restul impartirii
a = 2
print(3 != a)
print(3 <= a)
a += 5 #am adaugat valorii a insasi +5
print(a)

#Operatiuni cu strings
nume = "Ionescu"
print(nume.upper()) #scrie cu litere mari/ majuscule IONESCU
print(nume.lower()) #ionescu
print("iOnesCu".capitalize()) #Ionescu
titlu_film = "o noapte in paris"
print(titlu_film.title()) #O Noapte In Paris
print(nume.startswith("Ion")) #verificam daca string incepe cu "Ion", prefix
print(nume.endswith("scu")) #verificam daca se termina cu, sufix
print(nume.replace("n", "m"))  #inlocuieste n cu m, Iomescu
text = """
Aici este un text pe mai multe randuri. Vreau ca propozitiile sa le separ. Rezultatul va fi o lista cu fiecare
propozitie in parte. Separarea se va face dupa caracterul '.'.
"""
propozitiile = text.split(".")
print(propozitiile)

print("Ce mai \nfaci") #\n inseamna newline character
print(r"Ce mai \nfaci") #r inseamna raw string, adica nu interpreteaza caracterele speciale

lis_2 = ["Ion", "Ana", "Elena"]
string_din_lista = "-".join(lis_2)
print(string_din_lista)

#accesarea elementelor din lista
#dupa index
print(lis_2[0]) #indexarea in python incepe de la 0, nu de la 1
print(lis_2[1]) #[1] este elementul al doilea din lista
print(lis_2[3]) #IndexError: list index out of range, adica elementul al 4-lea nu exista

lis_3 = ["Ion", "Ana", ["nume_1", "nume_2"], "Elena"]
print(len(lis_3))
print(lis_3[2][1]) #accesare "etajata", element dintr-o lista din alta lista

#cu iteratie
for el in lis_3:
    print(el)

for indice, element in enumerate(lis_3):
    #print(indice, element)
    print(f"{indice +1} = {element}")
    #f-strings, adica un f inainte de " ne da posibilitatea sa adaugam variabile in string cu {}
    #enumerate este o functie care acceseaza indicele si valoarea in acelasi timp.

print(lis_3)
print(list(enumerate(lis_3))) #[(0, 'Ion'), (1, 'Ana'), (2, ['nume_1', 'nume_2']), (3, 'Elena')]
#am folosit functia list() pentru ca enumerate(x) este un generator (?)

str_3 = "Studentii de la SDA sunt faini"
#vreau sa verific daca sirul "sda" este in str_3
if 'sda'.lower() in str_3.lower():
    print('da')
else:
    print("nu") #estetic/stil e recomandat sa fim consistenti cu tipul de ghilimele ' sau "

print('sda'.lower() in str_3.lower())

print("ploaie" not in str_3)

lis_3 = ["Ion", "Ana", ["nume_1", "nume_2"], "Elena"]
print("Vasile" in lis_3, end="; ") #am adaugat un argument functiei print, rezultatul = False; True
print("Ana" in lis_3)
print(type("Ana" in lis_3)) #bool

ay = 1
if ay:
    print("da") #0 si 1 in python poate fi interpretat ca True sau False respectiv

check = 4 > 10
print(check)

if check:
    print("da")
else:
    print("nu")

by = ""
print(not by) #negarea valorii goale, adica not False
if not by: #if not False = if True. "" spatiul gol este interpretat ca False in python
    print("nu")

cy = []
if not cy:
    print("lista e goala")
else:
    print("lista nu e goala")

dx = dict() #{}
if not dx:
    print('dictionarul e gol')

a = True
b = False
print(a and b)
print(a or b)
print(not a)

print(int(a), int(b))
print(bool(0)) #False
print(bool(4)) #True, adica orice integer != 0 diferit de 0, va fi True
print(int('14')) #aici va functiona sa transformam "14" in 14
print(int('opt')) #ValueError: invalid literal for int() with base 10: 'opt'
#nu putem transforma acest string in integer

print(isinstance("14", int)) #Am verificat daca "14" este integer/int
print(isinstance(["12", 13], list)) #am verificat daca o valoare este de tip list(ă)

#Conventii estetice
#ex 1- denumirea functiilor si claselor
def adunarea_numerelor():
    pass #denumire functie snake_case

class CamelCaseExemplu: #exemplu de denumire CamelCase
    pass

#Style guide PEP-8 https://peps.python.org/pep-0008/
#https://google.github.io/styleguide/pyguide.html

l_1 = [1,2,3,4]
l_2 = [1,2,3,4]
print(l_1 == l_2)
print(l_1 is l_2) #l_1 si l_2 au aceleasi valori, DAR ocupa spatiu diferit in memorie!!!

l_3 = l_1
print(l_3 is l_1) #l_3 si l_1 ocupa acelasi spatiu in memorie
l_1.append(5)
print(l_1, l_3)

import copy
l_4_copy = copy.copy(l_1)
print(l_4_copy is l_1) #l_4_copy nu va avea acelasi spatiu in memorie cu l_1

"""
Aici este 
un comentariu 
pe mai multe linii
"""
# Aici este
# un comentariu
# pe mai multe linii

a: int = 5
a: str = "cinci"
print(a) #python este dynamically typed, adica variabilile pot sa-si schimbe tipul de date

#4, [2.3, 4.5], rezultatul = 2.3*4 + 4.5*4
#type hinting nu face obligatorie respectarea tipurilor de date
def muliplicare_numar(numar :int, lista: list[float]) -> float:
    #am declarat 2 argumente ale functiei
    #un argument mă aștept să fie integer, si al doilea argument o lista cu numere float/rationale
    #-> inseamna rezultatul functiei, ce tip de date returneaza
    rez = 0
    for el in lista:
        rez += numar*el

    return rez

print(muliplicare_numar(4, [2.3, 4.5]))
print(muliplicare_numar(2, [2.1, 4.1]))
print(muliplicare_numar(2.1, [2, 4.1]))

#Operatiuni cu fisiere
path_to_file = "B:/pyx/SDA/fsdbf.txt" #
folder = r"B:\pyx\SDA"
path_to_file_2 = f"{folder}/fsdbf.txt"
print(path_to_file_2)

with open(path_to_file, 'r') as alias_file:
    print(alias_file.read())

text_de_adaugat = "\nCe bucatarie preferi: italiana sau japoneza?"
with open(path_to_file, 'a') as f:
    f.write(text_de_adaugat)

folder_SDA_path = "B:/pyx/SDA"
#Creez un folder nou
import os
os.mkdir(f"{folder_SDA_path}/sda_51")

file_to_create = f"{folder_SDA_path}/sda_51/file_nou.txt"
text_1 = "Ce mai faci?"
with open(file_to_create, 'w') as f:
    f.write(text_1)

"""
In operatiunea cu fisiere, putem avea mai multe tipuri de operatii:
'r'- read
'w'- write, dar sterge mai intai si apoi scrie pe fisierul gol
'a' - append care adauga la textul existent
"""

a = 5
b = 6
c= 7
a, b, c = 5, 6, 7
print(b)

list_1 = [1,2]
list_1.append("Ceva")
print(list_1)
list_1.insert(1, 2.3)
print(list_1)
list_1.pop(2)
print(list_1)
list_1.pop(-1)
print(list_1)
list_1.remove(2.3)
print(list_1)

list_2 = [1, 2, 3, 2, 5, 2]
list_2.remove(2) #daca elementul nu este in lista, vom avea eroare
#ValueError: list.remove(x): x not in list
print(list_2)

def multiplicare(lista, numar =2):
    rez = 0
    for el in lista:
        rez += el*numar
    return rez

print(multiplicare([2,3,4]))

def adaugam_element(numar, lista =[]):
    #bad case practice- sa definim elemntele default al unei functii cu date mutable
    lista.append(numar**2)
    return lista

print(adaugam_element(3)) #expected result [9]
print(adaugam_element(4)) #expected [16], got [9,16]

def adaugam_element_v2(numar, lista =None):
    #in loc sa declaram default [], am declarat mai intai None, apoi lista []
    if not lista:
        lista = []
    lista.append(numar**2)
    return lista

print(adaugam_element_v2(3)) #[9]
print(adaugam_element_v2(4)) #[16]

#Mutable VS immutable
ax = 3
print(id(ax))
ax = 3+2
print(id(ax)) #integer este immutable, adica daca ii schimbam valoarea, se modifica si adresa in memorie
# a variabilei

lx = [1,2,3]
print(id(lx))
lx.append(6)
print(id(lx)) #am pastrat acelasi id in memorie, adica listele sunt obiecte de tip mutable
#adica isi pot schimba valoarea, si raman acelasi obiect in memorie
lx[2] = 7
print(lx)
print(id(lx))

tx = (1,2,3)
print(id(tx))
tx += (4,)
print(tx)
print(id(tx))
tx[2] = 7 #tuple e immutable, nu-si poate schimba valoarea odata creat.

#INCORECT, initializarea unui tuple cu un singur element
ty = (2)
print(ty, type(ty)) #2 <class 'int'>

#Corect
ty = (2,)
print(ty, type(ty)) #(2,) <class 'tuple'>

#initializarea unui tuple gol
tz = tuple()
print(tz, type(tz))

lz = list()
dz = dict()
sz = set()
print(sz, type(sz))

fisiere_list = ['n1', 'n2']
fisiere_set = {'n2', 'n2'}
if 'n1' in fisiere_list:
    print('da, list') #relativ mai incet decat apartenenta in set
#recomand
if 'n1' in fisiere_set:
    print('da, set')