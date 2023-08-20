from recap.helpx import ceva_functie

ceva_functie("bla bla")

import math
print(math.factorial(5)) #=1*2*3*4*5
print(math.sqrt(400))

# import os #am importat TOATA libraria os
from os import mkdir #am importat DOAR modulul mkdir din libraria os
folder_existent = "B:/pyx/SDA/sda_51"
# os.mkdir(f"{folder_existent}/folder_nou_sda51")
mkdir(f"{folder_existent}/folder_nou_sda51")

import psutil
proces_id = 33120
procesul = psutil.Process(proces_id)
memorie_ocupa = procesul.memory_info()

print(f"Procesul cu id-ul {proces_id} ocupa {memorie_ocupa} RAM bytes")

from os import mkdir as creaza_director #am dat un alias modulului mkdir

creaza_director(f"{folder_existent}/folder_dupa_alias")

