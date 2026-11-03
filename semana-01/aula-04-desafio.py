pontuacao = 30

if pontuacao >= 90 and pontuacao < 101:
    print('Classificação Excelente')
elif pontuacao >= 70 and pontuacao <= 89:
    print('Classificação Boa')
elif pontuacao >= 50 and pontuacao <= 69:
    print('Classificação Regular')
elif pontuacao >= 0 and pontuacao <= 49:
    print('Classificação Insuficiente')
else:
    print('Pontuação é inválida')