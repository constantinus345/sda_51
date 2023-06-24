#prima parte UPPER, a doua lower
strx = "Ce facem azi unde mergem grgdfhfbd fdsfsddsfdsgsdgd "
half_len = len(strx) // 2
rezult = strx[:half_len].upper() + strx[half_len:].lower()
print(rezult)

rez_25 = strx[:(len(strx) // 4)]
#putem pune un index nu doar ca numar, ci si ca expresie matematica
print(rez_25)

#len(strx) - tehnic e ok, dar e inutil lasat asa
print(len(strx))
lung = len(strx)

#ultimele 5 caractere invers
print(strx[-5:][::-1])
#e mai important codul sa fie usor de citit, decat prea "inteligent"/smecher

ax = 'Ana    are mere  si   pere'
rez_asteptat = 'Ana are mere si pere'
lista_cu_cuvinte = ax.split()
print(lista_cu_cuvinte) #['Ana', 'are', 'mere', 'si', 'pere']
#ca sa unim cuvintele despartite un un singur spatiu " ", folosim .join:
rez_unit = " ".join(lista_cu_cuvinte)
print(rez_unit)

#ex 25
print(len(strx))
#20
print(strx[:5]) #hardcoding of values!! NOPE

#' " """ '''
s1 = "Ana merge"
s2 = 'Ana merge'
s3 = """Ana merge"""
s4 = '''Ana merge''' #Toate sunt aceleasi string
#Ghilimele triple ne dau voie sa scriem multi-line
s5 = """Ana
Merge"""

nume = "Andrei"
print(f'El mi-a zis ca il cheama "{nume}"')
print(f"Salut {'_'*7} Ce mai faci")
#" El <<Andrei>>"


strx = "Ce facem azi unde mergem"
print(strx.replace("a", "x1").replace("e","x2"))
#Lant de replace

#Spatiile in python
#Unele reguli sunt pur-estetice/de stil, altele sunt functionale

nume="Ion"
nume = "Ion" #modul estetic de assignment, mai sus e mai greu de citit
print(7>9)
print(7 > 9)#e mai bine dpv estetic
print(f "Numele este {nume}") #spatiul f " este gresit

print(nume. replace("o", "u"). replace("I","x")) #e. r spatiul nu e ok

print(nume[2]) #estetic
print(nume[ 2 ]) #spatiul e ne-necesar dpv stil

#paranteze
strx = "Ce facem azi unde mergem"
print(strx[3]) #pentru index folsoim []
print(f"Al 4-lea caracter este {strx[3]}") #pentru variabile in f-string folosim {}
#pentru functii folosim ()

print(strx.lower) #<built-in method lower of str object at 0x0000022F3068A330>
print(strx.lower()) #() apeleaza functia

ax = 5
print(type(ax))
bx = float(ax)
print(bx, type(bx))
cx = str(ax)
print(f"cx = {cx} of type {type(cx)}")
# print(5 in ax) #error! because ax is integer, does not support "in" operation
print("5" in cx) #True


strx = "Ce facem azi unde mergem"
sub_1 = "ce"
sub_2 = "gem"
print(strx.lower().startswith(sub_1.lower())) #case insentitive check
print(strx.endswith(sub_2)) #case sensitive check