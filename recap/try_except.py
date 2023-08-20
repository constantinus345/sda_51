a = 9
b = 2
# print(a/b)

try:
    print(a/b)
#except: #except general nu este indicat
# except Exception as e:
#     print(f"Avem o exceptie: {e}")
except ZeroDivisionError:
    print("Nu se poate imparti cu 0")
finally:
    print("Voila, se executa no matter what, indiferent ca s-a executat la try sau la except")

a_2 = "Salut"
b_2 = 5
# print(a_2+b_2)
try:
    print(a_2+b_2)
except TypeError:
    print(f"Verifica type-urile variabilelor, a->{type(a_2)}, b->{type(b_2)}")

l_1 = [1,2,3]
print(l_1[5]) #IndexError

with open("whatever.txt", 'r') as f:
    text = f.read() #FileNotFoundError

folder = "abc"
try:
    with open(f"{folder}/whatever.txt", 'r') as f:
        text = f.read()
except FileNotFoundError:
    raise FileNotFoundError(f"Fisierul nu a fost gasit in folder-ul {folder}")

class FisierulInexistent(Exception):
    #Clasa custom made pentru a gestiona FileNotFound
    def __init__(self, file_name):
        self.file_name = file_name
        self.message = f"File {file_name} nu a fost gasit"
        super().__init__(self.message)

folder = "abc"
nume_fisier = "whatever.txt"
try:
    with open(f"{folder}/{nume_fisier}", 'r') as f:
        text = f.read()
except FileNotFoundError:
    raise FisierulInexistent(nume_fisier)

