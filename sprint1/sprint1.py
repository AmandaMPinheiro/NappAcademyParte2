import pickle 
         
#1
def prefixo_dr_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR'):
            sublista.append(item)
    return sublista

#2
def total_prefixo_dr_dra(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR'):
            total = total + 1
    return total

#3
def prefixo_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DRA'):
            sublista.append(item[0])
    return sublista

#4
def total_prefixo_dra(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DRA'):
            total = total + 1
    return total

#5
def prefixo_dr(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR.'):
            sublista.append(item[0])
    return sublista

#6
def total_prefixo_dr(lista):
    total = 0
    for item in lista:
        if item[0].upper().startswith('DR.'):
            total = total + 1
    return total

#7
def busca_sobrenomes(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome.upper() in item[0].upper():
            myTuple = (item[0], item[1])
            sublista.append(myTuple)
    return sublista

#8
def busca_sobrenomes_primeiros(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome.upper() in item[0].upper():
            myTuple = (item[0], item[1])
            sublista.append(myTuple)
    return sublista[:10]

#9
def busca_sobrenomes_ultimos(lista, sobrenome):
    sublista = []
    for item in lista:
        if sobrenome.upper() in item[0].upper():
            myTuple = (item[0], item[1])
            sublista.append(myTuple)
    return sublista[-10:]

#10
def busca_email(lista, email):
    registro = ()
    for item in lista:
        if email.upper() == item[2].upper():
            registro = item    
    return registro

#11
def busca_email_por_dominio(lista, dominio='gmail.com'):
    sublista = []
    for item in lista:
        dom = item[2].split('@')[1].upper()
        if dominio.upper() == dom:
            sublista.append(item)
    return sublista

#12
def busca_email_por_usuario(lista, username):
    sublista = []
    for item in lista:
        user = item[2].split('@')[0].upper()
        if username.upper() == user:
            sublista.append(item)    
    return sublista

#13
def busca_endereco(lista, endereco):
    sublista = []
    for item in lista:
        if endereco.upper() in item[7].upper():
            sublista.append(item)            
    return sublista

#14
def busca_estado(lista):
    sublista = []
    for item in lista:
        estado = item[7].split(' / ')[1].upper()
        sublista.append(estado)        
    sublista = list(set(sublista))    #set deixa valores únicos
    return sublista

#15
def busca_cartao_credito(lista, numero_cartao_procurado):
    sublista = []
    for item in lista:
        numCartao = item[8].split('\n')[2].split(" ")[0]
        if numero_cartao_procurado in numCartao:
            sublista.append(item)
    return sublista

#16
def busca_vencimento_cartao_credito(lista, mes_ano_vencimento):
    sublista = []
    for item in lista:
        if mes_ano_vencimento == item[9]:
            sublista.append(item)    
    return sublista

#17
def busca_mes_vencimento_cartao_credito(lista, mes_vencimento):
    sublista = []
    for item in lista:
        if str(mes_vencimento) in item[9].split('/')[0]:
            sublista.append(item)    
    return sublista

#18
def busca_ip(lista, ip_procurado):
    sublista = []
    for item in lista:
        if ip_procurado == str(item[5]):
            sublista.append(item)    
    return sublista

#19
def busca_prefixo_ip(lista, prefixo_ip='192'):
    sublista = []
    for item in lista:
        if prefixo_ip == str(item[5].split('.')[0]):
            sublista.append(item)    
    return sublista

#20
def busca_prefixo_sufixo_ip(lista, prefixo_ip='192', sufixo_ip='0'):
    sublista = []
    for item in lista:
        prefixo = item[5].split('.')[0]
        sufixo = item[5].split('.')[-1]        
        if prefixo == prefixo_ip and sufixo == sufixo_ip:
            sublista.append(item)        
    return sublista

if __name__ == "__main__":
    with open('lista.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)