import threading
from random import uniform
from time import sleep

# print(uniform(1.2, 3.4))

# def print_numere():
#     for nr in range(1, 11):
#         sleep(uniform(0.1,0.7))
#         print(nr)
#
# def print_litere():
#     for letter in "abcdefg":
#         sleep(uniform(0.1,0.7))
#         print(letter)
#
# t1 = threading.Thread(target=print_numere)
# t2 = threading.Thread(target=print_litere)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# #Exemplul 2
# def printeaza_ceva(nume):
#     print(nume)
#     sleep(uniform(0.1, 0.7))
#     print(f"{nume} are {len(nume)} caractere")
#     sleep(uniform(0.1, 0.7))
#     print(f"Primele 2 caractere ale {nume} sunt {nume[:2]}")
#
# def creaza_threaduri(o_lista_nume):
#     threads = list()
#     for un_nume in o_lista_nume:
#         t = threading.Thread(target=printeaza_ceva, args=(un_nume,))
#         threads.append(t)
#         t.start()
#
#     for tx in threads:
#         tx.join()
#
# lista_mea = ["Ana", "Ion", "Vasile", "Alexandru", "Alexandra"]
# creaza_threaduri(lista_mea)

import multiprocessing

def patrat(nr):
    sleep(uniform(8, 12))
    return nr**2
    sleep(uniform(2, 4))

if __name__ == "__main__":
    lista_patrate = list(range(11, 22))

    with multiprocessing.Pool() as pool:
        rezultate = pool.map(patrat, lista_patrate)

    print(rezultate)

#pentru multiThreading - un singur proces distribuit pe nucleele/threads ale procesorului
#e mai "light" la nivel de resurse (RAM, CPU etc)
#(tehnic- din cauza GIL global interpreter lock)- nu e "true" parallelism, totusi se executa un thread singur
#folosim cand avem limitari I/O input/output (citire network/ disk)

#multiProcessing - mai multe procese separate care executa in paralel instructiunile
#poate deveni "greu" dpv al consumului de resurse
#CPU-bound- cand procesorul are "spatiu" liber de manevra ca sa putem crea inca X procese separate.



