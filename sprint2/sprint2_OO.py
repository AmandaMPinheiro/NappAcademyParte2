import csv

class Sprint2:
    #16
    def __init__(self):
        self.lista = []
        
    #17
    def carregar_arquivo_para_lista(self, nome_arquivo):        
        with open(nome_arquivo, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row not in self.lista:
                    self.lista.append(tuple(row))
        self.lista = list(set(self.lista))
        
    #18
    def busca_trecho_nome(self, nome):
        saida = []
        for item in self.lista:
            if nome in item[0]:
                subtupla = (item[0], item[1])
                saida.append(subtupla)
        return saida

    #19
    def busca_email(self, email):
        saida = ()
        for item in self.lista:
            if email == item[2]:
                saida = item
        return saida

    #20
    def busca_estado(self):
        saida = []
        for item in self.lista:
            estado = item[7].split(' / ')[-1]
            if estado not in saida:
                saida.append(estado)
        return saida

    #21
    def busca_mes_vencimento_cartao_credito(self, mes_vencimento):
        saida = []
        for item in self.lista:
            if str(mes_vencimento) == item[9].split('/')[0]:
                saida.append(item)
        return saida

    #22
    def busca_prefixo_sufixo_ip(self, prefixo_ip='192', sufixo_ip='0'):
        saida = []
        for item in self.lista:
            prefixo = item[5].split('.')[0]
            sufixo = item[5].split('.')[-1]
            if prefixo == prefixo_ip and sufixo == sufixo_ip:
                saida.append(item)
        return saida

    #23
    def contar_ocorrencia_por_dominio_hostname(self, *dominios):
        lista_dom = []
        subdict = {}     
        for dominio in dominios:
            lista_dom.append(dominio)
            subdict[dominio] = 0
            
        for item in self.lista:
            dom = item[4].split('.')[-1]
            for dominio in lista_dom:
                if dominio == dom:
                    subdict[dominio] = int(subdict[dominio]) + 1                 
        saida = list(subdict.items())
        return saida
            
    #24
    def contar_ocorrencia_por_dominio_email(self, *dominios):
        lista_dom = []
        subdict = {}     
        for dominio in dominios:
            lista_dom.append(dominio)
            subdict[dominio] = 0
            
        for item in self.lista:
            dom = item[2].split('@')[1]
            for dominio in lista_dom:
                if dominio == dom:
                    subdict[dominio] = int(subdict[dominio]) + 1      
        saida = list(subdict.items())
        return saida
 
    #25   
    def busca_mes_aniversario(self, mes_aniversario):
        saida = []
        for item in self.lista:
            mes = item[3].split('-')[1]
            if int(mes_aniversario) == int(mes):
                saida.append(item)         
        return saida

    #26  
    def relatorio_lista_para_txt(self, arquivo, lista):
        with open(arquivo, 'w') as f:
            for registro in lista:
                f.write(40 * '*' + '\n')
                for i in range(len(registro)):
                    f.write(registro[i])
                    f.write('\n')
 
    def relatorio_lista_para_cvs(self, arquivo, lista):
        with open(arquivo, 'w') as f:
            writer = csv.writer(f)
            for registro in lista:
                writer.writerow(registro)
 
if __name__ == "__main__":
    objeto = Sprint2()
    objeto.carregar_arquivo_para_lista('arquivo_1.csv')
    objeto.carregar_arquivo_para_lista('arquivo_2.csv')
    objeto.carregar_arquivo_para_lista('arquivo_3.csv')
    
    
    # Descomentar para testar 
    # Relatório de pessoas com sobrenome 'Silva'
    lista = objeto.busca_trecho_nome('Silva')
    objeto.relatorio_lista_para_txt('relatorio_1.txt', lista)
    objeto.relatorio_lista_para_cvs('relatorio_1.csv', lista)
    # Relatório de tentativas de fraude com vencimento de cartão em dezembro
    lista = objeto.busca_mes_vencimento_cartao_credito('12')
    objeto.relatorio_lista_para_txt('relatorio_2.txt', lista)
    objeto.relatorio_lista_para_cvs('relatorio_2.csv', lista)
    
    