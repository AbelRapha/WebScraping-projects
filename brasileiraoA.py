import time
from requests import request
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# Pegar o conteudo HTML a partir da URL do sofascore
url = 'https://www.sofascore.com/tournament/football/brazil/brasileiro-serie-a/325'

option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)

driver.get(url)

driver.quit()
#Parsear o conteudo HTML com a BeutifulSoup

#Estruturar conteúdo em um data frame - Pandas

#Transformar Dados em um dicionário de dados próprio

#Converter e salvar em um arquivo jason