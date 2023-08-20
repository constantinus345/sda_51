from datetime import datetime
from time import perf_counter #calcularea performantei in timp al programului
from random import randint, choices #random stuff
import string #creeaza cuvinte cu caractere aleatorii
from sys import getsizeof

ora_acum = datetime.now().hour
print(ora_acum)
print(type(ora_acum))

def executa_doar_intre_orele(ora_inceput, ora_sfarsit):
    def decorator(func):
        def wrapper():
            print(f"Ora acum = {datetime.now().hour}")
            if ora_inceput <= datetime.now().hour <= ora_sfarsit:
                func()
        return wrapper
    return decorator

# def ----:
#     def decorator(func):
#         def wrapper():
#             -----
#         return wrapper
#     return decorator
#mai sus este "bioilerplate code", adica pentru a crea un decorator, asta e arhitectura codului

@executa_doar_intre_orele(6,11)
def trimite_email():
    print(f"Am trimis un email la toti angajati")

@executa_doar_intre_orele(1, 3)
def verifica_ceva():
    print("Am verifica sefu")

trimite_email()
verifica_ceva()

#Creez un decorator care masoara performanta de executare in timp a unui program


def masoara_performanta(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        time_took = perf_counter() - start_time
        print(f"Execution time = {round(time_took, 3)} secunde")
        return result
    return wrapper

@masoara_performanta
def list_random_size(size):
    random_strings = list()
    for i in range(size):
        lungime_random = randint(3,9)
        random_string = "".join(choices(string.ascii_letters, k= lungime_random))
        random_strings.append(random_string)
    return random_strings

lista_1 = list_random_size(10**7)

from time import sleep #sleep- face programul sa ia o pauza cateva secunde
@masoara_performanta
def ceva_functie():
    print("unu")
    sleep(5)
    print("doi")

ceva_functie()