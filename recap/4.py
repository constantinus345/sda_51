#pass, continue, break

listx = list(range(1, 13))
print(listx)

for x in listx:
    if x % 3 == 0:
        continue #cand ajunge la continue, reia bucla, ignorand instructiunile ramase in bucla
    print(x) #se va trece peste valorile ce se divid cu 3

for x in listx:
    if x % 3 == 0:
        pass #nu are nici o influenta
    print(x) #se vor printa toate valorile din lista

for x in listx:
    if x % 3 == 0:
        break
    print(x) #break sparge bucla si iese complet din ea.
def o_functie_complicata():
    pass
a = 1

