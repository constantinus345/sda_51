from time import perf_counter #calcularea performantei in timp al programului
from random import randint, choices #random stuff
import string #creeaza cuvinte cu caractere aleatorii
from sys import getsizeof

def list_random_size(size):
    random_strings = list()
    for i in range(size):
        lungime_random = randint(3,9)
        random_string = "".join(choices(string.ascii_letters, k= lungime_random))
        random_strings.append(random_string)
    return random_strings

print(list_random_size(4))

list_milion = list_random_size(10**7)
element_random_din_lista = list_milion[10**6 - randint(100, 10**5)]
print(f"Lungimea listei este {len(list_milion)}, iar un element random = {element_random_din_lista}")
set_milion = set(list_milion)

#Calculez performanta element in lista
time_start_1 = perf_counter()
if element_random_din_lista in list_milion:
    print("da")
took_list = perf_counter() - time_start_1
print(f"el in list luat {took_list} secunde")

#Calculez performanta element in set
time_start_2 = perf_counter()
if element_random_din_lista in set_milion:
    print("da")
took_set = perf_counter() - time_start_2
print(f"el in set luat {took_set} secunde")
print(f"f in set este de {round(took_list/took_set, 2)} ori mai rapid")

print(f"Lista cu {10**7} elemente are {getsizeof(list_milion)//2**20} Mbytes\nSetul are {getsizeof(set_milion)//2**20} Mbytes")

