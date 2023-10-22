import pickle
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

lista_mea = list_random_size(10**7)

folder = "B:/pyx/SDA/sda_51"
with open(f"{folder}/lista_107.pickle", "wb") as f:
    pickle.dump(lista_mea, f)

with open(f"{folder}/lista.pickle", "rb") as f_read:
    lista_mea_citita = pickle.load(f_read)

print(lista_mea_citita[:10])