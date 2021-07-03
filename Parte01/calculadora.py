valor = float(input("Valor que deseja investir: R$ "))

#Cada R$1, 30 pessoas visualizam 
visualizacoes_originais = valor * 30

#Cada 100 visualizaçoes, 12 pessoas clicam
max_cliques = (visualizacoes_originais*12)/100

#Cada 20 cliques, 3 pessoas compartilham
max_compartilhamentos = (max_cliques*3)/20

#Cada compartilhamento gera 40 novas visualizações
novas_visualizacoes = max_compartilhamentos*40

#Cada anúncio pode ser compartilhado no máximo 4 vezes em sequência
max_visualizacoes = novas_visualizacoes*4


print(max_visualizacoes)