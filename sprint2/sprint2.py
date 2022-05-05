import csv
from datetime import date
from collections import Counter
         
#01
def carregar_arquivo_para_lista(nome_arquivo):
    """
    Função recebe o nome de um arquivo csv e retorna a lista 
    de tuplas com 

    Args:
        nome_arquivo (string): Nome do arquivo CSV

    Returns:
        list: Lista com tuplas
    """
    lista = []
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lista.append(tuple(row))
    lista = lista[1:]
    return lista

#02
def carregar_arquivos_para_lista(*lista_arquivos):
    lista = []
    for nome_arquivo in lista_arquivos:
        with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                lista.append(tuple(row))
    return lista
    
#03
def busca_mes_vencimento_cartao_credito(lista, **parametros):
    try:
        mes = parametros['mes']
    except KeyError:
        mes = '03'
        
    try:
        ano = parametros['ano']
    except KeyError:
        ano = '23'
        
    sublista = []    
    for item in lista:
        data_venc = f'{mes}/{ano}'
        if str(item[9]) == data_venc:
            sublista.append(item)
    return sublista
    
#04
def contar_ocorrencias_cartao_credito_por_mes(lista):
    sublista = []
    for item in lista[1:]:
        sublista.append(item[9].split('/')[0])       
    saida = dict(Counter(sublista))
    return saida

#05
def contar_ocorrencias_cartao_credito_por_ano(lista):
    sublista = []
    for item in lista[1:]:
        sublista.append(item[9].split('/')[1])        
    saida = dict(Counter(sublista))
    return saida

#06
def busca_cvc(lista, cvc='043'):
    saida = []
    for item in lista:
        try:
            cod = item[8].split('CVC: ')[-1].strip()
            if str(cvc) == cod:
                saida.append(item)   
        except:
            continue
    return saida

#07
def busca_lista_cvcs(lista, *cvcs):
    if len(cvcs) == 0:
        cvcs = ('043')
    saida = []
    for item in lista:
        try:
            cod = item[8].split('CVC: ')[-1].strip()
            if str(cod) in cvcs:
                saida.append(item)   
        except:
            continue
    return saida

#08
def contar_ocorrencias_por_estado(lista):
    sublista = []
    for item in lista[1:]:
        estado = item[7].split(' ')[-1].strip()
        sublista.append(estado)
    saida = dict(Counter(sublista))
    return saida
       
#09
def busca_dados_navegador(lista, navegador='Chrome/24'):
    saida = []
    for item in lista:
        if navegador in item[6]:
            saida.append(item)
    return saida

#10
def contar_ocorrencias_por_sufixo_dominio(lista):
    sublista = []
    for item in lista[1:]:
        dominio = item[4].split('.')[-1]
        sublista.append(dominio)
    saida = dict(Counter(sublista))
    return saida

#11
def contar_ocorrencias_por_dominio_email(lista):
    sublista = []
    for item in lista[1:]:
        dominio = item[2].split('@')[-1]
        sublista.append(dominio)
    saida = dict(Counter(sublista))
    return saida

#12
def buscar_dominio_mais_utilizado(lista):
    sublista = []
    for item in lista[1:]:
        dominio = item[2].split('@')[-1]
        sublista.append(dominio)
        
    subdict = dict(Counter(sublista))
    subdict = list(subdict.items())
    
    indice = maior = i = 0
    for dom in subdict:
        valor = int(dom[1])
        if maior < valor:
            maior = valor
            indice = i
        i += 1
    saida = (subdict[indice][0], subdict[indice][1])
    return saida

#13
def contar_ocorrencias_por_semana(lista):
    sublista = []
    dias_semana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado', 'Domingo']
    for item in lista[1:]:
        data = item[3].split(' ')[0]
        ano, mes, dia = data.split('-')
        data = date(int(ano),int(mes),int(dia))
        sublista.append(dias_semana[data.weekday()])
    subdict = dict(Counter(sublista))
  
    saida = [('Segunda',subdict['Segunda']),
               ('Terça',subdict['Terça']),
               ('Quarta', subdict['Quarta']),
               ('Quinta',subdict['Quinta']),
               ('Sexta',subdict['Sexta']),
               ('Sábado',subdict['Sábado']),
               ('Domingo',subdict['Domingo'])]
    return saida
        
#14
def contar_ocorrencias_por_hora(lista):
    sublista = []
    for item in lista[1:]:
        hora = item[3].split(' ')[1].split(':')[0]
        sublista.append(hora)
    saida = dict(Counter(sublista))
    return saida

#15
def contar_ocorrencias_por_mes(lista):
    sublista = []
    for item in lista[1:]:
        mes = item[3].split('-')[1]
        sublista.append(mes)
    saida = dict(Counter(sublista))
    return saida

if __name__ == "__main__":
    lista = carregar_arquivo_para_lista('arquivo_1.csv')
