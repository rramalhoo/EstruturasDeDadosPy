cadastro = {}
continuar = 's'

print("CADASTRO")
while continuar == 's':
    nome = input("\nDigite o nome do aluno: ")
    idade = input("\nDigite a idade do aluno: ")
    curso = input("\nDigite o nome do curso: ")

    cadastro[nome] = {
        "Idade": idade,
        "Curso": curso
    }

    continuar = input("Dejesa continuar ? (s/n)")


for chave, valor in cadastro.items():
    print(f"\nNome: {chave} - Idade: {valor['Idade']} - Curso: {valor['Curso']}")