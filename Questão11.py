valor = input("Digite o valor da prestação ")
valor = float(valor)
tempo = input("Digite a quantidade de dias de atraso ")
tempo = int(tempo)
taxa = tempo * 5
prestação = valor + (valor *  (taxa/100) *  tempo)
print(prestação)
