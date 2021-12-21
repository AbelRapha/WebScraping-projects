import zapimoveis_scraper as zap
import requests as r
import io
import pandas as pd
import unidecode as code
import time

#Importando dados dos bairros do Brasil
df_bairros_municipios = pd.read_csv("Bairros.csv - Bairro.xlsx - Sheet 1.csv",error_bad_lines=False, sep=",")
df_bairros_municipios.drop(labels="Endereço", axis=1, inplace=True)

#Retornando no formato lista
list_municípios = df_bairros_municipios['Cidade'].to_list()
list_bairros = df_bairros_municipios['Bairros'].to_list()

#Realizando o enconding para realizar a pesquisa
list_municipios = [code.unidecode(cidade.replace(" ", "-").lower()) for cidade in list_municípios]
list_bairros = [code.unidecode(bairro.lower().replace(" ", "-")) for bairro in list_bairros]

#Unificando listas em um único data-frame
df_bairros_municipios = pd.DataFrame(data = zip(list_municipios,list_bairros))

#Municípios
rondonia = df_bairros_municipios.iloc[0:196,:]
amazonas = df_bairros_municipios.iloc[197:475,:]
roraima = df_bairros_municipios.iloc[476:530,:]
para = df_bairros_municipios.iloc[531:777,:]
amapa = df_bairros_municipios.iloc[778:818,:]
#Acre
#Distrito Federal
maranhao = df_bairros_municipios.iloc[819:859,:]
piaui = df_bairros_municipios.iloc[860:1240,:]
ceara = df_bairros_municipios.iloc[1241:2325,:]
rio_grande_do_norte = df_bairros_municipios.iloc[2326:2491,:]
paraiba = df_bairros_municipios.iloc[2492:2659,:]
pernambuco = df_bairros_municipios.iloc[2660:3186,:]
alagoas = df_bairros_municipios.iloc[3186:3308,:]
sergipe = df_bairros_municipios.iloc[3309:3396,:]
bahia = df_bairros_municipios.iloc[3397:3479,:]
minas_gerais = df_bairros_municipios.iloc[3480:5163,:]
espirito_santo = df_bairros_municipios.iloc[5164:5795,:]
rio_de_janeiro = df_bairros_municipios.iloc[5796:7039,:]
sao_paulo = df_bairros_municipios.iloc[7040:9016,:]
parana = df_bairros_municipios.iloc[9017:9772,:]
santa_catarina = df_bairros_municipios.iloc[9773:11219,:]
rio_grande_do_sul = df_bairros_municipios.iloc[11220:13199,:]
mato_grosso_do_sul = df_bairros_municipios.iloc[13200:13471,:]
mato_grosso = df_bairros_municipios.iloc[13472:14290,:]
goias = df_bairros_municipios.iloc[14291:14322,:]

list_bathrooms = []
list_value_rent = []
list_bedrooms = []
list_area_total = []
list_address = []
list_links = []
list_description = []

list_sp = []
for index, linha in sao_paulo.iterrows():
  list_sp.append(f"{linha[0]}++{linha[1]}")
list_anuncios_sp = []

anuncios = zap.search(localization="sp+ubatuba", num_pages=10,)


for atributo in anuncios:
    list_bathrooms.append(atributo.bathrooms)
    list_bedrooms.append(atributo.bedrooms)
    list_value_rent.append(atributo.price)
    list_area_total.append(atributo.total_area_m2)
    list_address.append(atributo.address)
    list_links.append(atributo.link)
    list_description.append(atributo.description)

# Colocando em um data frame
dicionario = {"Valor Aluguel": list_value_rent, 
              "Qtd Banheiros": list_bathrooms, 
              "Qtd Quartos": list_bedrooms, 
              "Area total" : list_area_total,
              "Endereço": list_address,
              "Link do Anúncio": list_links,
              "Descrição do Anúncio": list_description}

df_anuncios_casas_aluguel = pd.DataFrame.from_dict(dicionario, orient='index')
df_anuncios_casas_aluguel = df_anuncios_casas_aluguel.transpose()
 

# Exportando para um arquivo em csv
df_anuncios_casas_aluguel.to_csv("Anúncios de aluguel de casas.csv", sep=";", index=False)