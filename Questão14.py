altura = input("Digite a altura do triângulo")
altura = altura.replace(",",".")
altura = float(altura)
base = input("Digite o valor da base")
base = base.replace(",",".")
base = float(base)
area = (base * altura) / 2
print("Área do triângulo:", area)
