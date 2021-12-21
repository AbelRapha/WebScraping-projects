from os import name
from typing import Text
from bs4 import BeautifulSoup
from numpy import number
from numpy.core import numeric
from selenium import webdriver as web
import requests, time, random
from functions import create_dict,create_archive, length_of_archive, obtain_website ,read_text as txt
import pandas as pd


#Colocando os links em uma lista para não haver duplicidade na busca
list_links = list()
for i in range(length_of_archive("links.txt")):
    web_link = txt("links.txt", i)
    list_links.append(web_link)
    


#criando um timer
timer = 5

# Acessar a home do linkedin
option = web.ChromeOptions()
#option.headless = True
driver = web.Chrome(options=option)

# GET na URL
driver.get(txt("urls.txt", 1))

#Inserir o login e senha
login = txt("access.txt",1)
password = txt('access.txt',2)

#Encontrando os elementos para realizar o login
elementID = driver.find_element_by_id('username')
elementID.send_keys(login)

elementID = driver.find_element_by_id("password")
elementID.send_keys(password)

elementID.submit()

time.sleep(20)


number_of_pages = 2
content = list()
content_clean = list()
pages = 1
while(pages <= number_of_pages):
    if pages ==1:
      driver.get("https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22106057199%22%5D&industry=%5B%2244%22%5D&keywords=Transforma%C3%A7%C3%A3o%20Digital&origin=GLOBAL_SEARCH_HEADER")
      time.sleep(5)
      search_page = driver.find_elements_by_tag_name("a")
      for elemento in search_page:
        content.append(elemento.get_attribute('href'))
        for link in content:
            if "https://www.linkedin.com/company/" in link:
                if link not in content_clean:
                    content_clean.append(link)
                    
              
    else:
        driver.get(f"https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22106057199%22%5D&industry=%5B%2244%22%5D&keywords=Transforma%C3%A7%C3%A3o%20Digital&origin=GLOBAL_SEARCH_HEADER&page={str(pages)}")
        time.sleep(5)
        search_page = driver.find_elements_by_tag_name("a")
        for elemento in search_page:
            content.append(elemento.get_attribute('href'))
            for link in content:
                if "https://www.linkedin.com/company/" in link:
                    if link not in content_clean:
                        content_clean.append(link)
                        
    pages+=1


#Colocar no arquivo de texto

for link in content_clean:
    if link not in list_links:
        create_archive(link= link)
print(content_clean,len(content_clean))    
 


#Obter os links de cada empresa
# page_search = driver.find_elements_by_tag_name("a")

# for elemento in page_search:
#     content.append(elemento.get_attribute('href'))
#     for link in content:
#         if "https://www.linkedin.com/company/" in link:
#             if link not in content_clean:
#                 content_clean.append(link)








#Clicar e obter as informações de cada empresa




