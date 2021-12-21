from os import name
from typing import Text
from bs4 import BeautifulSoup
from numpy import number
from numpy.core import numeric
from selenium import webdriver as web
import requests, time, random
from functions import create_dict, length_of_archive, obtain_website ,read_text as txt
import pandas as pd

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

time.sleep(15)
#Fazendo a busca automática de acordo com os filtros realizado anteriormente
length = length_of_archive("urls.txt")

dictionary = {"Nome da Empresa": [], "Categoria": [],"website": [], "Qtd Funcionários": [], "Data da Fundação": [], "Localização":[]}

n =1

for link in range(2,length, 1):
 #Começo a contar a partir da segunda linha
    driver.get(txt("urls.txt",link))
    time.sleep(timer)
    
    driver.find_element_by_class_name("reusable-search__result-container").click()

    time.sleep(timer)

    current_url = driver.current_url
    new_url = current_url + "/" + "about" + "/"
    driver.get(new_url)

    time.sleep(15)

    main_element = driver.find_element_by_id("main")
    html__content = main_element.get_attribute('outerHTML')
    soup =  BeautifulSoup(html__content,'html.parser')

    #Get Name of Company
    try:
        name_company = soup.find('h1').get_text().strip()
        name_company = "".join(name_company)
        dictionary["Nome da Empresa"].append(name_company)
    except AttributeError:
        name_company = soup.find("span").get_text().strip()
        name_company = "".join(name_company)
        dictionary["Nome da Empresa"].append(name_company)

    #Get Category of company
    category = soup.find('div', attrs={'class': 'org-top-card-summary-info-list__info-item'}).get_text().split()
    category = " ".join(category)
    dictionary["Categoria"].append(category)
    
    #Get website
    about = soup.find_all("div", attrs={"class": "org-grid__content-height-enforcer"})
    website = about[0].find("span").get_text().split()
    website = website[0]
    dictionary["website"].append(website)

    #Get number of employees
    try:
        number_employees = about[0].find_all("dd", attrs={"class": "text-body-small t-black--light mb1"})[0].get_text().split()
        number_employees = number_employees[0]
        dictionary["Qtd Funcionários"].append(number_employees)
    except IndexError:
        number_employees = 0
        dictionary["Qtd Funcionários"].append(number_employees)

    #Get fundation time of company
    try:
        fundation_time = [objects for objects in about[0].find_all("dd", attrs={"class": "mb4 text-body-small t-black--light"}, text=True)]
        if len(fundation_time ) > 1:
                fundation_time = fundation_time[1].get_text().split()
                if fundation_time[0].isnumeric():
                    dictionary["Data da Fundação"].append(fundation_time[0])
                    
                else:
                    fundation_time = "Sem informação"
                    dictionary["Data da Fundação"].append(fundation_time)
        else:
            fundation_time = fundation_time[0].get_text().split()
            if fundation_time[0].isnumeric():
                dictionary["Data da Fundação"].append(fundation_time[0])
                
            else:
                fundation_time = 'Sem informação'
                dictionary["Data da Fundação"].append(fundation_time)
    except IndexError:
        fundation_time = "Sem informação"
        dictionary["Data da Fundação"].append(fundation_time)

    #Get local of company
    try: 
        content = about[0].find_all("p", attrs = {"class": "t-14 t-black--light t-normal break-words"})
        address_content = content[-1].get_text().split()
        local = " ".join(address_content[:-1])
        dictionary["Localização"].append(local)
    except IndexError:
        local = 'Sem informação'
        dictionary["Localização"].append(local)
    print(name_company, " " , local)
#Adicionando ao dicionario


#Criando e exportando para arquivo formato csv
df = pd.DataFrame.from_dict(dictionary, orient='index')
df = df.transpose()
df.to_csv('teste.csv', sep=";", index=False)


#Obtendo informações das empresas


# Sai do navegador
driver.quit()