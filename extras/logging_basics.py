#Cum fac un raport de executare al programului intr-un fisier de tip text
#ca sa analizez ulterior performanta programului meu

import logging
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
print(f"Azi este data - {today}")

#Creez o configurare pentru raportul de executare a codului
folder_logs = "B:/pyx/SDA/sda_51/Logs"
logging.basicConfig(filename=f"{folder_logs}/loguri_{today}.log",
                    format="%(asctime)s -- %(levelname)s -- %(message)s ",
                    filemode="a")
#Creez un obiect de manipulare a log-ului
obiect_logger = logging.getLogger()
obiect_logger.setLevel(logging.DEBUG)

#Nivele de mesaje in log
#debug - ne ofera informatii generale despre cod, informatii care nu afecteaza executarea programului
#info - similar
#warning
#error
#critical
#nivelurile de logging sunt mai mult conventii



def operatii_matematice(a,b):
    try:
        suma = a + b
        produsul = a * b
        impartirea = a / b
        raport = f"Rezultatele sunt suma = {suma}, produsul = {produsul}, impartirea = {impartirea}"
        print(raport)
        obiect_logger.info(f"Programul s-a executat cu succes, avand variabilele {a} si {b}")
    except Exception as e:
        print(e)
        obiect_logger.warning(f"Pentru variabilele {a} si {b} Programul a intampinat o eroare {e}")

operatii_matematice(7,9)
operatii_matematice(7,0)