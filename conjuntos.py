jogos = {"Valorant", "Fortnite", "Roblox"} #isso é um conjunto (não permite repetição de valor)
print("\nConjunto:\n")
print(jogos)
print("\n--------------------------------------")

#adicionando Minecraft
print("\nAdicionando Minecraft\n")
jogos.add("Minecraft")
print(jogos)
print("\n--------------------------------------")

#percorrendo o conjunto
print("\nPercorrendo o conjunto\n")
for jogo in jogos:
    print(jogo)
print("\n--------------------------------------")

#removendo "Fortnite"
print("\nRemovendo Fortnite\n")
jogos.remove("Fortnite")
print(jogos)
print("\n--------------------------------------")

#verificando a existência de um item:
print("\nVerificando a existência de um item\n")
jogo = input("Digite o nome do jogo:")

if jogo in jogos:
    print("\nJá existe esse jogo na lista")
else:
    print("\nNão localizado")

