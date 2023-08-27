import requests

from bs4 import BeautifulSoup as bs

link_1 = "https://pubmed.ncbi.nlm.nih.gov/29723297/"

raspuns = requests.get(link_1)
raspuns_soup = bs(raspuns.text, "html.parser")
clasa_doi = "identifier doi"
obiectul_doi = raspuns_soup.find("span", class_ = clasa_doi)
# print(obiectul_doi)
codul_doi = obiectul_doi.text.strip().replace("\n","").replace("DOI:", "").replace(" ","")
print(codul_doi)