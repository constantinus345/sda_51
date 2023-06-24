#radical
import math #importat toaaaaata libraria math
nr = 25
radical = math.sqrt(nr)
print(radical)

cosinus = math.cos(nr)
#pentru ca la import am importat toata libraria math, pot folosi si alte elemente din el
print(cosinus)

#V2 de import, import doar o bucatica din librarie
from math import sqrt
nr = 25
radical = sqrt(nr)
print(radical)

#V2 alias
from math import sqrt as radacina
nr = 25
radical = radacina(nr)
print(radical)

lista_nr = [1,2,3,4]
avg_1 = sum(lista_nr)/ len(lista_nr)
#metoda 2 pentru average
from statistics import mean
print(mean(lista_nr))

#Importam toate modulele din librarie
from math import * #code smell
#DON'T DO IT!
print(sqrt(9))
print(factorial(5))

#Best case - importam doar ce ne trebuie, evitam alias-urile, de exemplu
from math import sqrt

#Built-in libraries, de ex: statistics, math, os
import os

path = "B:\Dropbox\SDA\SQL F44 exer"
toate_fisierele = os.listdir(path)
print(toate_fisierele)

#calc_suma din ceva_functie
from Predare.ceva_functie import calc_suma
#Am importat din fisierul ceva_functie, care se afla in folderul Predare
#Am importat functia calc_suma, ca sa n-o mai scriu o data aici

print(calc_suma(1,2,3,4,5,6))

