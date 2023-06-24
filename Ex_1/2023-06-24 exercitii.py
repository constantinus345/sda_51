#Definiti o functie care returneaza suma patratelor a doua numere
def suma_patratelor(a,b):
    return a**2 + b*b #fie scriem la patrat, sau inmultim de doua ori

print(suma_patratelor(3,4))

# Definiti o functie care printeaza suma patratelor a doua numere, dar nu returneaza nimic
def sum_patrate_print(a,b):
    print(f"Suma patratelor lui {a} si {b} = {a**2 + b**2}")

sum_patrate_print(3,5)

#Definiti o functie care returneaza suma patratelor a X (nedefinit) numere, doar daca sunt impare
def suma_patrate_impare(*args):
    suma = 0
    for nr in args:
        if nr % 2 == 1:
            suma += nr**2

    return suma

rez = suma_patrate_impare(1,2,3,4,5,6)
print(rez)