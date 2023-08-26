#Simple :
#int, float, bool, str
#Complexe: list, set, dict, tuple

#Queue
from collections import deque

qx = deque()
qx.append("1")
qx.append("2")
qx.append("3")
qx.append("4")

print(qx)
v1 = qx.popleft()
print(v1)
print(qx)

v4= qx.pop()
print(f"v4 = {v4}, qx_ramas = {qx}")

"""
Diferenta dintre queue si list: 
la list putem adauga si scoate elemente doar din dreapta
la queue putem face aceste operatiuni din ambele capete
"""

#Frozen set
set_simplu = {1,2,3,4}
set_frozen = frozenset([1,2,3,4])
print(set_simplu)
print(set_frozen)

#Counter - de cate ori s-a repetat un element intr-o lista
#returneaza un dictionar Counter cu cheie: nr de repetari
from collections import Counter
lisx = ["n1", "n2", "n3", "n2", "n2", "n1"]

count = Counter(lisx)
print(count)

#OrderedDict

dict_1 = dict()
dict_1['d'] = 3
dict_1['c'] = 9
dict_1['a'] = 2
print(dict_1) #dict simplu poate reprezenta datele intr-o ordine haotica a cheilor
#nu neaparat in ordinea in care am adautgat
for k, v in dict_1.items():
    print(k,v)

del dict_1['c'] #am sters un element
print(dict_1)

from collections import OrderedDict

dict_2 = OrderedDict()
dict_2['d'] = 3
dict_2['c'] = 9
dict_2['a'] = 2

print(dict_2) #OrderedDict mentine ordinea adaugarii elementelor
element_x = dict_2.pop('c') #am sters un element
#del sterge pur-si-simplu un element dintr-un dictionar,
#pe cand pop sterge si poate stoca valoarea intr-o variabila
print(dict_2)
print(element_x)
#dict este prin definitie neordonat, adica nu conteaza ordinea elementelor in dictionar
#OrderedDict este ordonat, similar ca o lista sau tuple.

from collections import namedtuple

Oras = namedtuple("Orasul", ['nume', 'populatie', 'suprafata_km2'])
Iasi = Oras("Iasi", "300000", "30")
Cluj = Oras("Cj", "400000", "50")
print(Iasi)

#nametuple poate fi accesat dupa index si dupa numele cheii
#dictionarul poate fi accesat doar dupa cheie

print(Iasi[1])
print(Iasi.populatie)
Iasi[1] = 400000

#namedtuple nu isi poate modifica valorile odata create
#OrderedDict putem modifica valorile

