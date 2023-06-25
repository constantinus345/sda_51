#Object Oriented Programming
class Animal:
    Era_Curenta = "Modern Age" #variabile ale clasei
    Total_animals = 0

    def __init__(self, nume, varsta):
        #initializarea variabilelor obiectelor particulare
        #__init__ este o metoda speciala de initializare
        #functiile in interiorul claselor se numesc metode ale clasei

        self.nume = nume #asa se initializeaza valoarile obiectelor cu self.variabila= variabila
        self.varsta = varsta
        Animal.Total_animals += 1

    def prezinta_animalul(self):
        print(f"{self.nume} are varsta de {self.varsta} ani")
        #metode care pot doar executa instructiuni si nu returneaza nici o valoare

    def echivalare_umana(self):
        return self.varsta + 7
        #aici avem o metoda care returneaza valoare
        #pentru a accesa variabilele unei instante, e necesar doar sa specificam self


tigrul_meu = Animal("Boby", 12) #am creat o instanta a clasei Animal cu doua variabile
tigrul_meu.prezinta_animalul() #am accesat o metoda a clasei care executa cod, dar nu returneaza valori
print(tigrul_meu.nume) #am accesat variabila instantei
print(tigrul_meu.varsta)
echivalent_uman_tigru = tigrul_meu.echivalare_umana() #am calculat valoarea obiect.metoda, pentru ca avem return
print(echivalent_uman_tigru)

cainele_meu = Animal("Puppy", 3) #am initializat un alt obiect
cainele_meu.prezinta_animalul()
print(cainele_meu.varsta)
print(cainele_meu.echivalare_umana())
print(f"Am un catel excelent pe nume {cainele_meu.nume} de varsta {cainele_meu.varsta}")
#Am accesat variabilele obiectului in interiorul f-string
print(Animal.Total_animals) #Am accesat variabila clasei, se schimba in dependenta de numarul de obiecte
print(Animal.Era_Curenta) #Aceasta variabila a clasei e indenpendenta de numarul de obiecte

class Contacte:

    def __init__(self, prenume, email, telefoane, cod_secret, cod_secret_2 = "secret default"):
        self.prenume = prenume
        self.email = email
        self.telefoane = telefoane
        self._cod_secret = cod_secret #_ este o conventie pentru a arata care variabile nu sunt intentionate
        #de a fi apelate in afara functiei
        #o sugestie pentru ceilalti developers
        self.__cod_secret_2 = cod_secret_2 #o variabila privata a instantei, care nu poate fi accesata in afara functiei
        #_ = conventie de privat, but not enforced (adica putem totusi accesa valoarea)
        #__ = variabila privata impusa/enforced, adica nu o putem accesa in afara clasei


    def apelez(self):
        print(f"Doriti sa apelati un numar de telefon din lista {self.telefoane}, alegeti un numar de la 1 la {len(self.telefoane)}")
        indexul = input("Spuneti care numar de telefon, indicele = ")
        print(f"Acum apelam numarul {self.telefoane[int(indexul) - 1]}")

    def privat_impus(self):
        print(f"Variabila super secreta este {self.__cod_secret_2}")

John = Contacte("Johnny", ["john@gmail.com"], [123, 456, 789], "fjkhsg3279", "fds")
# John.apelez()
print(John._cod_secret)
# print(John.__cod_secret_2) #va da eroare, variabila nu poate fi accesata
John.privat_impus() #aici va printa, adica variabila este accesata in interiorul unor metode, dar nu direct

Ana = Contacte("a", [], [], 23) #am initializat un obiect, ale carui parametri ii vom schimba ulterior
Ana.prenume = "Ana"
Ana.email = ["ana@gmail.com", "ana2@me.me"] #Schimb valorile obiectului
Ana.telefoane = ["012", "+40145", 777898555]
print(Ana) #<__main__.Contacte object at 0x000001DFEDABF850>, adica un obiect al clasei Contacte
Ana.apelez()

#Am avut o intrebare cu procesarea in masa a contactelor din excel.
#Grosso-modo putem face ceva de genu
Lista_Excel = {"prenume":["Vasile", "Elena"],
               "emailuri":[["v@v.com"], ["e@e.ci", "e2@e.c"]],
               "telefoane":[[12,23], [18,19,22,24]],
               "coduri":[12,13]}

for i in range(len(Lista_Excel["prenume"])):
    Contacte(Lista_Excel["prenume"][i],
             Lista_Excel["emailuri"][i],
             Lista_Excel["telefoane"][i],
             Lista_Excel["coduri"][i])

class Person:
    def __init__(self, nume, varsta):
        self.__nume = nume
        self.__varsta = varsta

    def prezentare(self):
        print(f"Numele meu este {self.__nume}")

    def ce_varsta(self):
        if isinstance(self.__varsta, int) and self.__varsta >0:
            return self.__varsta
        return None

George = Person("George", 1)
George.prezentare()
print(George.ce_varsta())
print(George.__varsta) #EROARE, __varsta e atribut privat

class Person_2:
    def __init__(self, nume, an_nastere):
        self.nume = nume
        self.an_nastere = an_nastere
    @property
    def varsta(self):
        return 2023 - self.an_nastere

Vasile = Person_2("Vasilica", 1990)
print(Vasile.varsta) #pentru ca am folosit @property, varsta o pot accesa fara a o apela
#varsta devine un atribut al obiectului, nu o metoda()

class Om:
    def __init__(self, prenume, varsta, nationalitate, skills):
        self.prenume = prenume
        self.varsta = varsta
        self.nationalitate = nationalitate

class Student_SDA(Om):
    #Clasa Student_SDA va mosteni/ inheritance de la clasa Om
    def __init__(self, prenume, varsta, nationalitate, skills):
        super().__init__(prenume, varsta, nationalitate)
        #super() ne mosteneste atributele de la clasa superioara Om
        self.skills = skills

# class Contabil(Om)

class SDA_Microsoft(Student_SDA):
    def __init__(self, prenume, varsta, nationalitate, skills, departament):
        super().__init__(prenume, varsta, nationalitate, skills)
        self.departament = departament

Razvan = Student_SDA("Razvan", 29, "Ro", ["Python", "Baze de date"])
print(Razvan.prenume)

Ana = SDA_Microsoft("Ana", 25, "Ro", ["python", "C", "SQL", "multe altele"], "Security")
print(Ana.departament)

class Om:
    def __init__(self, prenume):
        self.prenume = prenume

class Student(Om):
    def __init__(self, prenume, materii_studiate):
        super().__init__(prenume)
        self.materii_studiate = materii_studiate

class Angajat(Om):
    def __init__(self, prenume, functie):
        super().__init__(prenume)
        self.functie = functie

class Angajat_Student(Student, Angajat):
    def __init__(self, prenume, materii_studiate, functie, ore_saptamana):
        Student.__init__(self, prenume, materii_studiate)
        Angajat.__init__(self, prenume, functie)
        self.ore_saptamana = ore_saptamana

S_1 = Angajat_Student("Ion", "econ", "Ospatar", 20)
print(S_1.prenume)


