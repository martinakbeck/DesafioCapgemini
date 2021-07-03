import funcoes


menu = 0
while menu != 3:
    menu = int(input("""O que deseja realizar?
    1- Cadastra novo anúncio
    2- Consultar
    3- Sair
    """))
    if menu == 1:
        print(funcoes.incluir_cadastro())
    elif menu == 2:
        op = int(input("""Qual opção de filtro
        1 - Por cliente
        2 - Por data
        """))
        if op == 1:
            print(funcoes.consulta_cliente())
        elif op == 2:
            print(funcoes.consulta_data())
        else:
            print("Opção inválida")
    elif menu != 3:
        print("Opção inválida")
    else:
        break





