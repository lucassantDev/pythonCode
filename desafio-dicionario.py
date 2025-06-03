aluno = {
    "Aluno": [],
    "Nota": []
}

nome = str(input("Informe o nome do aluno: "))
aluno['Aluno'].append(nome)
nota = float(input('Informe a nota: '))
aluno['Nota'].append(nota)
print(aluno)
pergunta = float(input('Quer continuar? \n 1- sim \n 2- não \n'))
while True:
    nome = str(input("Informe o nome do aluno: "))
    aluno['Aluno'].append(nome)
    nota = float(input('Informe a nota: '))
    aluno['Nota'].append(nota)
    pergunta = str(input('Quer continuar? \n 1- sim \n 2- não \n'))
    while pergunta == 1:
        continue
        if pergunta == 2:
            break
    break
   
    
    