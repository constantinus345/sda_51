#functie care genereaza o lista cu numere haotice
from random import randint
from copy import deepcopy
def gen_lista_random(nrx):
    lisx = []
    for i in range(nrx):
        lisx.append(randint(1,10**6))
    return  lisx


#algoritmul binar


def binary_search(lista, nr_de_cautat):
    """
    :param lista: lista sortata de numere
    :param nr_de_cautat
    :return: indexul unde a fost gasit elementul nr_de_cautat
    """
    low = 0
    high = len(lista) - 1

    while low <= high:
        #impartim lista in jumate, si ne oprim doar cand n-o mai putem divide
        mid = (low + high)//2
        #am calculat indexul din mijloc unde voi imparti lista in 2
        if lista[mid] == nr_de_cautat:
            return f"Indexul unde am gasit numarul {nr_de_cautat} este {mid}"
        elif lista[mid] < nr_de_cautat:
            low = mid + 1 #voi lua lista din dreapta
        else:
            high = mid -1 #voi lua lista din stanga

    return f"Nu am gasit acest numar"

lix = [1,3,12, 15, 29, 45, 200, 456]
nrx = 3
print(binary_search(lista= lix,
                    nr_de_cautat= nrx))

alta_lista = []
alt_numar = 2
print(binary_search(lista= alta_lista,
                    nr_de_cautat= alt_numar))
#lista si nr_de_cautat sunt parametrii functiei, care primesc ca valori alte variabile

#Algoritmul de bubble sort
def bubble_sort(lista_neordonata):
    #traversam lista
    operatii = 0
    for i in range(len(lista_neordonata)):
        for j in range(0, len(lista_neordonata)- i -1):
            #schimbam cu locul elementele, daca primul e mai mare ca urmatorul
            if lista_neordonata[j] > lista_neordonata[j+1]:
                lista_neordonata[j], lista_neordonata [j+1] = lista_neordonata [j+1], lista_neordonata[j]
                operatii += 1
                #a, b = b, a -aici am schimbat cu locul valorile
    print(f"S-au efectuat {operatii} pt bubble_sort")
    return lista_neordonata #aici deja devine practic lista_ordonata

lista_haotica = [123, 321, 426,4324, 76, 23, 3125, 5213543, 34, 231]
print(bubble_sort(lista_haotica))
#print(bubble_sort(lista_neordonata = lista_haotica))


lista_haotica.sort()
print(lista_haotica)

#Insertion sort
def insertion_sort(lisn):
    #Traversam lista incepand cu al doilea element
    counter = 0
    for i in range(1, len(lisn)):
        #selectam elementul curent
        k = lisn[i]
        j = i -1
        while j >= 0 and k < lisn[j]:
            lisn[j+1] = lisn[j]
            j += -1 #j = j-1 sau j -= 1
            counter += 1
        lisn[j+1] = k
    print(f"S-au efectuat {counter} pt insertion_sort")
    return lisn



#Merge sort
def mergex(lista_stanga, lista_dreapta):
    #initializam o lista goala, rezultatul
    rez = []
    #initializam cate un index pentru doua lista
    i = j = 0
    #Combinam doua liste pana cand una din ele este goala
    while i < len(lista_stanga) and j < len(lista_dreapta):
        if lista_stanga[i] < lista_dreapta[j]:
            rez.append(lista_stanga[i])
            i += 1
        else:
            rez.append(lista_dreapta[j])
            j += 1

    rez.extend(lista_stanga[i:])
    rez.extend(lista_dreapta[j:])
    return rez

#diferenta dintre append si extend
# lisx1 = [1,2,3]
# lisx1.append([22,33])
# print(lisx1)
# lisx1.extend([55,66])
# print(lisx1)
def merge_sort(lista):
    #impartim lista in doua sub-liste egale
    mid = len(lista) // 2
    lista_stangax = lista[:mid]
    lista_dreaptax = lista[mid:]
    #sortam prin metoda recurenta, functia apeleaza la ea insasi
    lista_stangax = merge_sort(lista_stangax)
    lista_dreaptax = merge_sort(lista_dreaptax)
    return mergex(lista_stangax, lista_dreaptax)






#selection sort

def selection_sort(lista):
    counter = 0
    #traversam lista
    for i in range(len(lista)):
        initial_i = i
        #traversam lista ramasa dupa i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[initial_i]:
                initial_i = j
                counter += 1
        lista[i], lista[initial_i] =  lista[initial_i], lista[i] #swap intre elemente
    print(f"S-au efectuat {counter} pt selection_sort")
    return lista

lista_haotica_1 = gen_lista_random(80)
lista_haotica_2 = deepcopy(lista_haotica_1)
lista_haotica_3 = deepcopy(lista_haotica_1)
# print(lista_haotica)
print(lista_haotica_1 is lista_haotica_2)
print(bubble_sort(lista_haotica_1))
print(insertion_sort(lista_haotica_2))
print(selection_sort(lista_haotica_3))

#quicksort algo
def quicksorting(lista):
    if len(lista)<= 1:
        return lista

    mijloc = lista[ len(lista)//2 ] #elementul de la mijlocul listei
    #len(lista)//2 - indexul de mijloc al listei

    stanga = [x for x in lista if x < mijloc ]
    dreapta = [x for x in lista if x > mijloc]
    mijloc = [x for x in lista if x == mijloc ]

    return quicksorting(stanga) + mijloc + quicksorting(dreapta)

lista_haotica_1 = gen_lista_random(81)
lista_haotica_2 = deepcopy(lista_haotica_1)
lista_haotica_3 = deepcopy(lista_haotica_1)
lista_haotica_4 = deepcopy(lista_haotica_1)
# print(lista_haotica)
print(lista_haotica_1 is lista_haotica_2)
print(bubble_sort(lista_haotica_1))
print(insertion_sort(lista_haotica_2))
print(selection_sort(lista_haotica_3))

lista_quicksorted = quicksorting(lista_haotica_4)
print(lista_quicksorted)