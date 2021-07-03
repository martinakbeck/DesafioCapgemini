from datetime import datetime

#Cálculo de visualizações, cliques e compartilhamento
def calculadora_alcance(valor):
    global max_cliques, max_compartilhamentos, max_visualizacoes
    visualizacoes_originais = valor * 30
    max_cliques = (visualizacoes_originais*12)/100
    max_compartilhamentos = (max_cliques*3)/20
    novas_visualizacoes = max_compartilhamentos*40
    max_visualizacoes = novas_visualizacoes*4
    print(max_visualizacoes)
    return max_cliques, max_compartilhamentos, max_visualizacoes

#Gravar dados do anúncio
def incluir_cadastro():
    global nome_cliente, nome_anuncio, data_inicio, data_termino
    global max_cliques, max_compartilhamentos, max_visualizacoes, valor_total
    nome_cliente = input("Informe nome do Cliente: ")
    nome_anuncio = input("Informe nome do Anúncio: ")
    data_inicio = input("Informe data de início (dd/mm/aaaa): ")
    data_termino = input("Informe data de término (dd/mm/aaaa): ")
    valor_dia = int(input("Informe valor de Investimento por dia: "))
    qtd_dias(data_inicio, data_termino)
    valor_total = total_dias*valor_dia
    calculadora_alcance(valor_total)
    gerar_dicionario(nome_anuncio, nome_cliente, data_inicio, data_termino, valor_total, max_visualizacoes, max_cliques, max_compartilhamentos)

#Cálculo de quantos dias de duração o anúncio terá 
def qtd_dias(inicio, termino):
    global total_dias
    d1 = datetime.strptime(inicio, '%d/%m/%Y')
    d2 = datetime.strptime(termino, '%d/%m/%Y')
    total_dias = abs((d1-d2).days)
    return total_dias

    
#Gera dicionário para gravar no relatório
def gerar_dicionario(anuncio, cliente, inicio, termino, valor, visualizacoes, compartilhamentos, cliques):
    pass


def criar_relatorio(dic):
    arquivo = open("relatorio.txt", "a")
    arquivo.close()

    arquivo = open('relatorio.txt', 'r') # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append(str(dic))   # insira seu conteúdo

    arquivo = open('relatorio.txt', 'w') # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo) # escreva o conteúdo criado anteriormente nele.
    arquivo.writelines("\n")    

    arquivo.close()



def consulta_cliente():
    cliente=input("Informe nome do cliente para consulta: ")
    arquivo = open('Desafio02/relatorio.txt', 'r')
    arquivo.readlines()
    for linha in arquivo:
        if linha.find(cliente) :
            print(linha)
    arquivo.close()


def consulta_data():
    data=input("Informe nome do cliente para consulta: ")
    arquivo = open('relatorio.txt', 'r')
    for linha in arquivo:
        if linha.find(data) > -1:
            print (linha)
