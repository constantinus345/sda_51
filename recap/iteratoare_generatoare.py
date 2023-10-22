lista_mea = [1, 2, 3]
for element in lista_mea:
    print(element)

lista_cu_next = iter(lista_mea)
print(next(lista_cu_next)) #next da posibilitatea sa extragem elemente dintr-o lista unu cate unu
#pana se epuizeaza lista si primim o eroare StopIteration

class Patrate:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            result = self.i**2
            self.i += 1
            return result
        else:
            raise StopIteration

squares = Patrate(10)
for p in squares:
    print(p)

patrate = [x**2 for x in range(11)]
print(patrate)
for x in patrate:
    print(x)

#generator pentru patrate

def patrate_generator(de_la, pana_la):
    for nr in range(de_la, pana_la+1):
        yield nr**2

patratele_10_20 = patrate_generator(10, 20)

print(list(patratele_10_20))

print(patratele_10_20)
for el in patratele_10_20:
    print(el)

def patrate_lista(de_la, pana_la):
    lis_patrate = []
    for nr in range(de_la, pana_la+1):
        lis_patrate.append(nr**2)
    return lis_patrate

patrate_milion_generator = patrate_generator(10, 10**6)
patrate_milion_lista = patrate_lista(10, 10**6)

from sys import getsizeof
print(f"Size of generator = {getsizeof(patrate_milion_generator)} bytes")
print(f"Size of list = {getsizeof(patrate_milion_lista)} bytes")
print(f"Lista ocupa de {getsizeof(patrate_milion_lista)//getsizeof(patrate_milion_generator)} mai multe ori spatiu ca generatorul")

print(range(1,20))
print(list(range(1,20)))