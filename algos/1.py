#factorial - produsul de la 1 la n.
#5! = 1*2*3*4*5

from time import  perf_counter
def masoara_performanta(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        time_took = perf_counter() - start_time
        print(f"Execution time = {round(time_took, 3)} secunde")
        return result
    return wrapper

@masoara_performanta
def factorial_v1(n):
    rezultat = 1
    for i in range(1, n+1):
        rezultat *= i
    return rezultat


#metoda recurenta, adica functia se apeleaza pe ea insasi
def factorial_recurent(n):
    if n == 0:
        return 1
    return n * factorial_recurent(n-1)

numar = 100
time_start_clasic = perf_counter()
print(factorial_v1(numar))
print(f"Clasic took = {perf_counter() - time_start_clasic}")
time_start_rec = perf_counter()
print(factorial_recurent(numar))
print(f"Recurent took = {perf_counter() - time_start_rec}")

#Sirul lui Fibonacci : 1,1,2,3,5,8,11,19,....
def fibo_clasic(n):
    a, b = 1, 1
    if n in (1,2):
        return 1
    for i in range(2, n):
        c = a+b
        a=b
        b=c
    return b

def fibo_recurent(n):
    if n <= 1:
        return n
    return fibo_recurent(n-1) + fibo_recurent(n-2)

numar = 400
start_clasic = perf_counter()
print(f"clasic {numar} = {fibo_clasic(numar)}")
took_clasic = perf_counter() - start_clasic
print(f"Clasic took = {took_clasic} secunde")

start_recurent = perf_counter()
print(f"recurent {numar} = {fibo_recurent(numar)}")
took_recurent = perf_counter() - start_recurent
print(f"Recurent took = {took_recurent} secunde")
print(f"Recurent a luat de {took_recurent // took_clasic} ori mai mult timp")

