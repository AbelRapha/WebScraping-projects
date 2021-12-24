import pandas as pd


def read_text(name_archive, number_of_line):
    """
    This function read archives txt e return elements line by line

    name_archive (str): Name of the archive in format txt
    number_of_line (int): Number of line the archive txt
    """
    file =  open(name_archive)
    lines = file.readlines()
    return lines[number_of_line-1] #Pega apenas o trecho da linha em específico
    #return lines

def length_of_archive(name_of_archive):
    """
    This function read archive txt e return a length of the archive. Basically count all lines
    in this archive

    name_of_archive (str): Name of the archive txt 
    """
    file = open(name_of_archive)
    return len(file.readlines())

def obtain_website(html):
    for a in html:
        return a['href']

def create_dict(name=None, category=None, website=None, range_employees=None, fundation_time=None,Local=None):
    dictionary = dict()
    dictionary['Nome da Empresa'] = name
    dictionary['Categoria'] = category
    dictionary['website'] = website
    dictionary['Qtd de Funcionários'] = range_employees
    dictionary['Data da fundação'] = fundation_time
    dictionary['Localização'] = Local
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    df = df.transpose()
    return df


def create_archive(link):
    with open("links.txt", "a+") as file:
        #verify if have content in archive
        file.seek(0)
        #if file is not empty the append "/n"
        data = length_of_archive('links.txt')
        if data > 0:
            file.write("\n")
            #append text at the end of file
            file.write(str(link))
        else: 
            file.write(str(link))
        
    
