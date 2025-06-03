#https://www.resiclean.com.br/gerenciamento-residuos-pesagem/
print("Cashback Verde")
nome = input('Olá! Informe seu nome: ')
print(f'Olá {nome}! Bem-vindo ao nosso sistema de cashback.')
material = int(input('Qual material você busca descartar corretamente: \n 1- Plástico \n 2- Vidro \n 3- Alumínio \n 4- Ferro \n 5- Outro \n resposta: '))
if material == 1:
    kg_informados = float(input('Informe o Kg da sua pesagem: '))
    preco-plastico = 0
    print(f'Levando em consideração recentes pesquisas, o valor da sua pesagem referente a esse resíduo será de R${preco}. Esse valor será convertido em um cashback para trocar nos produtos dos seguites nichos:')
elif material == 2:
    kg_informados = float(input('Informe o Kg da sua pesagem: '))
    preco_vidro = 0.12 * kg_informados
    print(f'Levando em consideração recentes pesquisas, o valor da sua pesagem referente a esse resíduo será de R${preco_vidro}. Esse valor será convertido em um cashback para trocar nos produtos dos seguites nichos:')
elif material == 3:
    kg_informados = float(input('Informe o Kg da sua pesagem: '))
    preco-aluminio = 0
    print(f'Levando em consideração recentes pesquisas, o valor da sua pesagem referente a esse resíduo será de R${preco}. Esse valor será convertido em um cashback para trocar nos produtos dos seguites nichos:')
elif material == 4:
    kg_informados = float(input('Informe o Kg da sua pesagem: '))
    preco-ferro = 0
    print(f'Levando em consideração recentes pesquisas, o valor da sua pesagem referente a esse resíduo será de R${preco}. Esse valor será convertido em um cashback para trocar nos produtos dos seguites nichos:')