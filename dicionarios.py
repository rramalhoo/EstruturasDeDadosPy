aluno = {} #dicionario vazio

#adicionando dados no dicionario
print("\nAdicionando dados:\n")
aluno["Nome"]= input("Digite o nome o aluno: ")
aluno["Idade"]= input("Digite a idade do aluno: ")
aluno["Curso"]= input("Digite o curso do aluno: ")
print("\n-------------------------------------------------------------------------------------------\n")

#acessando valores em um dicinário
print("\nAcesando valores:\n")
print(aluno["Nome"])
print(aluno["Idade"])
print(aluno["Curso"])
print("\n-------------------------------------------------------------------------------------------\n")
print(f"{aluno["Nome"]} - {aluno["Curso"]} ")

#alterar um valor
print("\n-------------------------------------------------------------------------------------------\n")
print("Alterando o valor:\n")
aluno["Idade"]=18
print(aluno)

#adicionar uma nova chave
print("\n-------------------------------------------------------------------------------------------\n")
print("Adicionando uma nova chave:\n")
aluno["Cidade"] = "São Paulo"
print(aluno)

#remover chave
print("\n-------------------------------------------------------------------------------------------\n")
print("Removendo chave:\n")
del aluno["Cidade"]
print(aluno)

#percorrendo chave
print("\n-------------------------------------------------------------------------------------------\n")
print("Percorrendo chave:\n")
for chave, valor in aluno.items():
    print(f"{chave} - {valor}")
