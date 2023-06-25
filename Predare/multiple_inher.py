class Om:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

class Robot:
    def __init__(self, brand, membre):
        self.brand = brand
        self.membre = membre
class Angajat:
    def __init__(self, cost, functie):
        self.cost = cost
        self.functie = functie

class AngajatOm(Om, Angajat):
    def __init__(self, nume, varsta, cost, functie):
        Om.__init__(self, nume, varsta)
        Angajat.__init__(self, cost, functie)


class AngajatRobot(Robot, Angajat):
    def __init__(self, brand, membre, cost, functie, nume_robot):
        Robot.__init__(self, brand, membre)
        Angajat.__init__(self, cost, functie)
        self.nume_robot = nume_robot

    def servire(self):
        print(f"Salut, numele meu este robot {self.nume_robot} si sunt produs de compania {self.brand}. Cu ce pot sa va servesc?")

# ion = AngajatOm("Ion", 23, 12000, "bucatar")
# print(ion.varsta)

robo_osptar_1 = AngajatRobot("Sony", 8, 30000, "Ospatar", "Willy")
print(robo_osptar_1.functie)
print(robo_osptar_1.nume_robot)
robo_osptar_1.servire()
