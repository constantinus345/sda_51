#pip install pandas, pentru date de tip tabelar
import pandas as pd
#trebuie sa instalam si openpyxl cu pip
#pip install openpyxl

tabel_dict = {"col_1":[1,2,3],
         "col_2":[11,22,33]}

tabel_pandas = pd.DataFrame(tabel_dict)
print(tabel_pandas)

folder_existent = "B:/pyx/SDA/sda_51"
#Vreau sa creez un fisier excel cu tabelul de mai sus

tabel_pandas.to_excel(f"{folder_existent}/ex_tabel.xlsx", sheet_name="pagina_1", index=False)

#Citesc din fisier excel existent
tabel_citit = pd.read_excel(f"{folder_existent}/ex_tabel.xlsx")
print(tabel_citit)

