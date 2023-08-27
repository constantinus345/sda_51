import asyncio

import requests

from bs4 import BeautifulSoup as bs
# Pentru a citi elementele unei pagini html, folosesc libraria beautifulsoup
# pip install beautifulsoup4

#Aceasta functie returneaza titlul unei pagini wikipedia
async def titlu_wiki(link_pagina):
    loop = asyncio.get_running_loop()
    raspuns = await loop.run_in_executor(None, requests.get, link_pagina)
    #am inspectat pagina web, si am gasit clasa tagului cu titlul paginii de wikipedia
    clasa_titlu = "firstHeading mw-first-heading"

    textul_paginii = raspuns.text
    supa_textului = bs(textul_paginii, "html.parser")

    titlul = supa_textului.find("h1", class_ = clasa_titlu)
    return titlul.text

Linkuri = ["https://ro.wikipedia.org/wiki/Europa_Central%C4%83",
           "https://ro.wikipedia.org/wiki/Liechtenstein",
           "https://ro.wikipedia.org/wiki/Asocia%C8%9Bia_European%C4%83_a_Liberului_Schimb",
           "https://ro.wikipedia.org/wiki/Regatul_Unit_al_Marii_Britanii_%C8%99i_al_Irlandei_de_Nord",
           "https://ro.wikipedia.org/wiki/Canalul_M%C3%A2necii",
           "https://ro.wikipedia.org/wiki/Marea_Nordului"]

async def executa_citirea():
    taskuri_asincrone = []
    for url in Linkuri:
        task = asyncio.create_task(titlu_wiki(url))
        taskuri_asincrone.append(task)
    titlurile = await asyncio.gather(*taskuri_asincrone)
    for titlu in titlurile:
        print(titlu)

if __name__ == "__main__":
    asyncio.run(executa_citirea())