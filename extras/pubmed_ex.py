import requests
from bs4 import BeautifulSoup as bs

def get_doi_id(link_pubmed):
    raspuns = requests.get(link_pubmed)
    raspuns_soup = bs(raspuns.text, "html.parser")
    clasa_doi = "identifier doi"
    obiectul_doi = raspuns_soup.find("span", class_ = clasa_doi)
    # print(obiectul_doi)
    codul_doi = obiectul_doi.text.strip().replace("\n","").replace("DOI:", "").replace(" ","")
    return codul_doi

print(get_doi_id("https://pubmed.ncbi.nlm.nih.gov/29723297/"))