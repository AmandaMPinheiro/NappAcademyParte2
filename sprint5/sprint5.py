import os
import glob
import csv

#1
def todos_arquivos_txt():
    looking_for = '**/*.txt'
    matched = glob.glob(looking_for, recursive=True)
    return matched

#2
def todos_arquivos_csv():
    looking_for = '**/*.csv'
    matched = glob.glob(looking_for, recursive=True)
    return matched

#3
def carregar_arquivo_txt_para_lista(nome_arquivo):
    lista = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace('\n','')
            linha = linha.split('\t')
            linha = linha[0:-1]
            lista.append(tuple(linha))
    return lista

#4
def carregar_arquivo_csv_para_lista(nome_arquivo):
    lista = []
    with open(nome_arquivo, 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            lista.append(tuple(linha))
    return lista[1:]

#5
def buscar_trecho_nome(lista, trecho_nome):
    sublista = []
    for item in lista:
        if trecho_nome in item[0]:
            sublista.append(item)
    return sublista

#6
def buscar_nome(lista, nome_procurado):
    sublista = []
    for item in lista:
        if nome_procurado == item[0]:
            sublista.append(item)
    return sublista

#7
def buscar_email(lista, email):
    sublista = []
    for item in lista:
        if email == item[2]:
            sublista.append(item)
    return sublista

#8
def buscar_cpf(lista, cpf):
    sublista = []
    for item in lista:
        if cpf == item[1]:
            sublista.append(item)
    return sublista

#9
def buscar_trecho_cpf(lista, trecho_cpf):
    sublista = []
    for item in lista:
        if trecho_cpf in item[1]:
            sublista.append(item)
    return sublista

#10
def buscar_dominio_email(lista, dominio):
    sublista = []
    for item in lista:
        if len(item) == 0:
            continue
        if dominio in item[2]:
            sublista.append(item)
    return sublista

#11
def buscar_trecho_nome_email(lista, trecho_nome, email):
    sublista = []
    for item in lista:
        if email in item[2] and trecho_nome in item[0]:
            sublista.append(item)
    return sublista

#12
def gravar_lista_para_arquivo_csv(lista, nome_arquivo):
    with open(nome_arquivo,'w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(['Nome', 'CPF', 'E-mail'])
        wr.writerows(lista)


if __name__ == '__main__':
    root_dir = os.getcwd()
    new_dir = os.getcwd() + '/arquivos/'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_1 = buscar_dominio_email(ocorrencias, 'ig.com.br')

    os.chdir(root_dir)   
    os.mkdir('relatorio') 
    new_dir = os.getcwd() + '/relatorio'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_2 = buscar_dominio_email(ocorrencias, 'ig.com.br')

    
    # NESTE TRECHO, ALTERAR O DIRETÓRIO DE TRABALHO
    # Os arquivos gerados com as funções abaixo devem gerar arquivos
    # dentro do diretório relatorio. Este diretório deve ser criado via script também
    
    gravar_lista_para_arquivo_csv(dominio_ig_1, 'dominio_ig_all.csv')
    gravar_lista_para_arquivo_csv(dominio_ig_2, 'dominio_ig_dir6.csv')
