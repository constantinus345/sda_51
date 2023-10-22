def add_squares_v1(a, b):
    return a**2 + b**2

print(add_squares_v1(3,4))

add_squares_v2 = lambda a,b : a**2 + b**2
print(add_squares_v2(3,5))

par_sau_nu = lambda x: x % 2 == 0
print(par_sau_nu(17))
print(par_sau_nu(170))

primele_chars = lambda strx, x : strx[:x] #extrage primele x caractere dintr-un string
print(primele_chars('Afara ploua frumos', 7))

#echivalent cu
def primele_chars_v2(strx, x):
    return strx[:x]

print(primele_chars_v2('Afara ploua frumos', 7))

min_lista = lambda lisx: min(lisx)
lista_ex = [23, 54, 19, 2, 100]
print(min_lista(lista_ex))

#pytest-nope
#threading, multiprocessing