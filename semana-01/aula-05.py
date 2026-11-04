nome = input("Digite o nome do avaliado: ")

idade = int(input("Digite a idade: "))

pontuacao = int(input("Digite a pontuação: "))

if pontuacao < 0 or pontuacao > 100:
    print("Pontuação inválida")

elif pontuacao >= 90:
    print(f"Classificação de {nome} está Excelente")

elif pontuacao >= 70:
    print(f"Classificação de {nome} está Boa")

elif pontuacao >= 50:
    print(f"Classificação de {nome} está Regular")

else:
    print(f"Classificação de {nome} está Insuficiente")