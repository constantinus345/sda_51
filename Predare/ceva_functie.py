def calc_suma(*args):
    rez = 0
    for n in args:
        rez += n
    return rez

# print(calc_suma(1,2,3,4))

#daca nu vreau instructiunile de mai sus la print sa fie executate cand importam functia in alta parte
#folosim urmatorul cod:
if __name__ == "__main__":
    print(calc_suma(1, 2, 3, 4))