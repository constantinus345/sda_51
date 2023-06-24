"""O sa va impart aleatoriu in 2 breakout rooms pentru a crea 2 echipe. Cineva din echipa va partaja ecranul, și astfel veți rezolva impreună. Eu voi merge în fiecare grupă câteva minute pana terminati, ca eventual sa va ajut
Scrieti un sir de caractere pe care veti face operatiuni.
afisati o jumate de sir cu uppercase, cealalta jumate cu lowercase. (hint, posibila solutie: functia len, operatorul //)
extrageti primele 25% caractere din sir
afisati un string care zice cate caractere sunt in acel string, ceva de genul "Sirul de mai sus are 17 caractere"
inlocuiti un cuvant din text cu alt cuvant. (hint: functia replace, detalii găsiți la un search pe google)
***a căuta soluții pe net este un skill important la un programator, chiar dacă pare trivial.
verificati daca un cuvant este parte din acel sir.
verificati daca un cuvant NU este parte din acel sir
Inversati ultimele 5 caractere din sirul de caractere scris la inceput. De exemplu pentru "Salut ce faceai" = "iaeca".
eliminati spatiile duble din textul "Salut        ce mai   faci   ?" (hint: tot cu functia replace)
Inlocuiti vocalele a si o cu x1, respectiv x2.
Calculati restul impartirii lui a la b si afisati patratul restului impartirii lui a la b. De ex a= 7, b = 5, se va afisa: "Patratul restului impartirii lui 7 la 5 este 4"
Scrieti o variabila nume, dati o valoare si apoi creati o alta variabila care va fi mereu egala cu "Salut <nume>, ce mai faci". De exemplu daca nume = "John", cealalta variabila va fi "Salut John, ce mai faci".
Compara daca doua siruri sunt egale, ignorand case-ul. De exmplu "salut lume" = "SaLuT LuMe" True.
Calculeaza (a la puterea b)/(b la puterea a), rotunjit la trei decimale, apoi afiseaza rezultatul formatat "frumos"/usor de intels.
Verificati daca un numar contine cifra 7 (hint: cautati pe net cum se face transformarea din integer in string, apoi in)
Extrageti subtextul pana la prima virgula intalnita intr-un string. Hint: strx.index(",")
Verificati daca un text incepe cu un prefix anume.
Aveti 3 numere a, b, c. Calculati cate cifre au totate 3 in total. De ex 1, 12, 1346 au 7 cifre."""

#afisati o jumate de sir cu uppercase, cealalta jumate cu lowercase
text = "Salut, Lume!"
#Comm: nu hard-coding
#Comm: "It's here" - difference between " ' and """
#Comm : len(strx) - se executa, dar nu e util.
#Comm: reverse_order: fie in doi pasi, sau strx[-5:][::-1]
#Comm: replace chaining sau itself replacing
#Denumirea modulelor/fisierelor: doar cu a-zA-Z0-9_, am vazut ex10.06.py la Ana Beiu
#Comm: String mereu in ghilimele
#Comm: Spatiile in python, incl f-string, functii
#Comm: importance of exercise and superior vs perfect student
#lower() si lower
#transformarea variabilelor- de ce avem nevoie de ea, operatiile pe tipuri de date, si erori (gen int("sapte"))
#startswith and endswith
#Cand se folosesc parantezele


half_length = len(text) // 2
result = text[:half_length].upper() + text[half_length:].lower()
print(result)

#extrageti primele 25% caractere din sir
quarter_length = len(text) // 4
first_quarter = text[:quarter_length]
print(first_quarter)

#invers 5
initial_text = "Salut ce faceai"
last_five_reversed = initial_text[-5:][::-1]
print(last_five_reversed)

#Replace only with one space any amount of spaces
ax = 'Ana    are mere  si   pere'
lista_text = ax.split()
ax_un_spatiu = " ".join(lista_text)
print(ax_un_spatiu)



