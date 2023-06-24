def denumire(variabila_1):
    if variabila_1 % 2 == 0:
        variabila_1 += variabila_1 -1
    else:
        variabila_1 += variabila_1 + 1
    return variabila_1

rezultat = denumire(23) #47
print(rezultat)
print(denumire(12)) #23
print(denumire(17)) #35

"""
Functiile reprezinta o incapsulare de mai multe instructiuni. 
Cuvantul cheie pentru a incepe o functie este def
Functiile pot executa instructiuni cu sau fara a returna o valoare
Daca nu folosim return, functia are valoarea None
"""

def suma(a,b,c):
    rez = a + b + c
    print(rez)
    return rez

#a,b,c se numesc argumente ale unei functii, adica variabilele ce vor fi folosite in interiorul functiei
#pot exista functii fara argumente!
#pot exista functii fara a returna o valoare

print(suma(2,3,4))

def salutare(): #aici functia nu accepta nici un argument, si nici nu returneaza o valoare
    #la apelarea functiei salutare(), doar se va executa print-ul
    print("Salut, ce mai faci?")

salutare()
val_salutare = salutare()
print(val_salutare) #A exectat print-ul din interiorul functiei, dar a returnat None
#pentru ca nu am folosit return la nici o valoare

print(salutare) #<function salutare at 0x000001A073A98B80>
#Aici nu executam functia, ci doar facem referire la ea.

def print_par(nra):
    print(f"Numarul {nra} este par")
    #nra este variabila locala a functiei

def print_impar(nrb):
    print(f"Numarul {nrb} este impar")

def ce_fel_de_numar(nr_intreg):
    if nr_intreg % 2 == 0:
        print_par(nr_intreg) #apelez functia de mai sus print_par
        #funcia a luat un argument, nu neaparat cu acelasi nume cu care a fost definita
        #argumentele functiilor sunt locale, adica nu sunt definite in afara functiei
    else:
        print_impar(nr_intreg)

ce_fel_de_numar(47)
print(nr_intreg) #EROARE, nr_intreg este definit doar pentru functia de mai sus
#adica este variabila locala

#In cazul de mai sus, verifica paritatea numarului, si in dependenta de rezultat
#apeleaza o alta functie


var_1 = 10

def inmultire_ceva(var_2):
    return var_2 * var_1

rez_1 = inmultire_ceva(15)
print(rez_1) #a inmultit variabila locala 15 / var_2 cu variabila locala 10 /var_1
#pentru ca functia de mai sus a returnat o valoare, rez_1 devine 150
#mai jos functia nu returneaza nimic, deci rez_2 are valoarea None

var_1 = 10
def inmultire_ceva_fara_return(var_2):
    print(var_2 * var_1)

rez_2 = inmultire_ceva_fara_return(13)
print(rez_2) #rez is None

var_globala = "Salut"

def zice_ceva(var_locala):
    print(f"Variabila globala este >>{var_globala}<<")
    print(f"Variabila locala este >>{var_locala}<<")

zice_ceva("ionel")

print(f"Variabila globala este >>{var_globala}<<") #se va executa in afara functiei
print(f"Variabila locala este >>{var_locala}<<") #eroare, var_locala nu exista in afara functiei


#*args ne da voi sa dam un numar nedeterminat de argumente unei functii
def suma_numere(*args):
    sumx = 0
    for a in args:
        sumx += a
    return sumx

rez = suma_numere(1,2,3,4,7)
print(rez)

def salutare_each(*args):
    for a in args:
        print(f"Salutare {a}")

nume = ["Ion", "Elena", "Ana", "Vasile"]
salutare_each(nume) #!!! Salutare ['Ion', 'Elena', 'Ana', 'Vasile'], adica lista e un singur argument
salutare_each("Ion", "Elena", "Ana", "Vasile")
salutare_each("Ion", "Elena")

def salutare_din_lista(lix): #folosim lista ca argument, nu args, varianta 2
    for num in lix:
        print(f"Salutare {num}")

salutare_din_lista(nume)

def raport(prenume, varsta, cnp):
    raportul = f"Cetateanul {prenume} de {varsta} ani are CNP = {cnp}"
    return raportul

rez_1 = raport("Ion", 25, 1234)
print(rez_1) #aici am respectat ordinea argumentelor definita in functie
#la rez_4 nu am respectat ordinea, implicit rezultatul e incorect

rez_2 = raport(prenume= "Vasile", varsta=34, cnp=1298747)
print(rez_2)

rez_3 = raport(cnp=14234, prenume="Ana", varsta=43)
print(rez_3) #daca denumim variabilele, ordinea nu este strict necesara

rez_4 = raport(42346372, "Elena", 32)
#!!! ASA NU, fie respectam ordinea argumentelor, cum sunt definite in functie
# fie le denumim ca la rez_3 sau rez_2
print(rez_4)

#Default function arguments
def raport_cu_default(prenume, varsta, cnp, tara = "Romania"):
    #tara este argument cu valoare default
    raportul = f"Cetateanul {prenume} de {varsta} ani are CNP = {cnp}, si e din {tara}"
    return raportul

rez_5 = raport_cu_default(prenume= "Vasile", varsta=34, cnp=1298747)
print(rez_5)

rez_6 = raport_cu_default(prenume= "Giovanni", varsta=35, cnp=1293458747, tara= "Italia")
print(rez_6) #pentru ca tara a fost schimbata, nu va mai scrie in raport Romania, ci Italia

rez_7 = raport_cu_default("Vasile", 34, cnp=1298747, tara="Suedia")
print(rez_7) #E posibil sa facem o combinatie dintre a respecta ordinea variabilelor si a le denumi
#Nu recomand dpv estetic (python style)

#Type hints
def raport_cu_hints(prenume:str, varsta:int, cnp:int, tara:str="Romania") -> str:
    raportul = f"Cetateanul {prenume} de {varsta} ani are CNP = {cnp}, si e din {tara}"
    return raportul
    #return 12 daca functia returneaza alt tip de date decat cel de la type hint
    #primim un warning, dar oricum se executa

print(raport_cu_hints("Ana", "22", 2424532))

a = 7
a = "sapte"
print(a) #python este "dynamically typed" adica o variabila poate avea mai multe tipuri de date
#in alte limbaje de programare acest lucru e mult mai strict
#de aceea s-au implimentat type hints, care nu sunt obligatorii/restrictii la executarea codului

def zile_cu_vant(data_azi, *args):
    #*args e o conventie in python pe care va recomand s-o respectati
    #Adica in loc de *args putem pune alt nume, ex *zile
    print(f"Astazi e data de {data_azi}")
    for zi in args:
        print(f"{zi} va fi vant puternic")

zile_cu_vant("24 Iunie", "Luni", "Vineri")
zile_cu_vant("24 Iunie") #*args sunt optionale

def constructor_reteta(denumire_reteta, **kwargs):
    #**kwargs = keyword arguments
    #adica cheie=valoare in cantitate nedeterminata, adica putem avea oricate chei=valori
    print(f"Aici sunt ingredientele pentru reteta {denumire_reteta}")
    for key, value in kwargs.items():
        print(f"{key} = {value} unitati")

    # for key in kwargs.keys(): #aici accesez doar cheile kwargs
    #for val in kwargs.values() #aici accesez doar valorile
    #.items() acceseaza atat cheile cat si valorile in ordinea cheie, valoare.

constructor_reteta("mamaliga", faina_pop=200, sare=5, apa=300)
constructor_reteta("ochiuri", oua=3, sare=2, piper=2, unt=30)