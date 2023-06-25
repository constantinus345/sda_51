Folder = "B:/Dropbox/SDA/SDA_51"
#https://pathcopycopy.github.io/ - program care copie path-urile, mai sus am folosit "unix path" cu /

# Folder = "B:\nicolae" #\n este interpretat ca newline
# Folder = r"B:\nicolae" #r tranbsforma in raw-string, adica nu interpreteaza caractere precum \n ca newline
# print(Folder)

nume = "Elena"
varsta = 22
#Vreau sa scriu intr-un fisier .txt "Elena este nascuta in anul 2001"
path = f"{Folder}/primul_text.txt"
operatiunea_write = "w" #w inseamna operatiunea de scriere
#daca exista text, il va sterge si va scrie din nou.
text = f"{nume} este nascuta in anul {2023 - varsta}"
with open(path, operatiunea_write) as alias:
    alias.write(text)

#Daca vreau sa adaug la ceea ce era deja scris
path = f"{Folder}/primul_text.txt"
operatiunea_append = "a"
text_nou = "\nIn casa arde focul"
with open(path, operatiunea_append) as f:
    f.write(text_nou)

#Operatiunea de citire
fisier = "ceva_text_creat.txt"
path = f"{Folder}/{fisier}"
operatiunea_citire = "r"
with open(path, operatiunea_citire) as alias:
    textul_meu = alias.readlines()
    print(textul_meu)

with open(path, operatiunea_citire) as alias:
    textul_meu = alias.readlines()
    for line in textul_meu:
        print(line)

with open("B:/Dropbox/SDA/SDA_51/fisier_2.txt", "w") as file:
    file.write("Ceva text aici")

#tipuri de operatiuni: w, a, r
#write, append, read

#alte operatiuni:
#x - operatiune de scriere NUMAI daca fisierul NU exista
#b - deschidere fisier in binary mode, de obicei non-text files
