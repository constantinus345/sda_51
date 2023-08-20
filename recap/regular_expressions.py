import re

text = """
Ion are marimea 46 la incaltaminte, si are doar 18 ani. Anisoara are marimea 40, si are 26 ani. 
Ambii sunt nascuti intr-o localitate cu mai putin de 12400 oameni.
Afara sunt 34 grade Celsius.
"""

numerele = re.findall(r"\d+", text)
print(numerele)

preturi = ["Ciocolata 10.87", "Vodka 19.30", "Branza 17.56"]
pattern_cautat = r'\d+\.\d+'
#\d - matches digits
#+ - one or more occurences
#. inseamna orice caracter. Dar pentru matching al "." propriu-zis, folosim \.
#patternul de mai sus va face matching doar pe numar.numar

for el in preturi:
    pret_gasit = re.findall(pattern_cautat, el)
    print(pret_gasit)

telefoane = ["Ion +40789 ", "Vasile +097654367842523 ", "Ana +77895 ", "Elena +45456 +48987456244"]
pattern_telefon_5 = r"\+\d{5}\D"
for tel in telefoane:
    tel_gasit = re.findall(pattern_telefon_5, tel)
    if len(tel_gasit) >0:
        print(tel_gasit)

preturi = ["Ciocolata 10.87", "Vodka 19.30", "Branza 17.56"]
#vreau sa substitui toate preturile cu X.Y
pattern_cautat = r'\d+\.\d+'
replacement = "X.Y"
for produs in preturi:
    text_nou = re.sub(pattern_cautat, replacement, produs)
    print(text_nou)

text = "Afara ploua frumos si Ion se joaca cu lego apoi alt Ion face altceva"
text_cautat = "Ion"
locatia = re.search(text_cautat, text)
print(locatia) #returneaza pozitia inceput-sfarsit al primului element gasit.

text_email = "Emailul meu personal este nume.prenume@gmail.com, iar cel de la munca este prenume@sda.ro "
email_pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.\w{2,5}\W"
are_email = re.search(email_pattern, text_email)
print(are_email)

text = "Ion, Elena; Ana-Andrei"
split_pattern = r",|;|-"
lista_split = re.split(split_pattern, text)
print(lista_split) #despart elementele textului fie dupa , sau ; sau -
