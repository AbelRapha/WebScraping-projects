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

time.sleep(10)

content = list()
content_clean = list()
for linha_url in range(2,length_of_archive("urls.txt")+1):
    driver.get(txt("urls.txt",linha_url ))
    time.sleep(10)
    url = driver.current_url
    number_of_pages = int(input("Digite o número de páginas de busca: "))
    pages = 1
    while(pages <= number_of_pages):
        driver.get(url+f"&page={pages}")
        time.sleep(5)
        search_page = driver.find_elements_by_tag_name("a")
        for elemento in search_page:
            content.append(elemento.get_attribute('href'))
            for link in content:
                if "https://www.linkedin.com/company/" in link:
                    if link not in content_clean:
                        content_clean.append(link)
        print(content_clean)
                
        pages+=1

    #Colocar no arquivo de texto

    text = txt("links.txt", length_of_archive("links.txt"))
    for link in content_clean:
        if link not in text:
            create_archive(link= link)  