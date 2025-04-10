base = input("Digite o valor da base")
base = base.replace(",",".")
base = float(base)
altura = input("Digite o valor da altura")
altura = altura.replace(",",".")
altura = float(altura)
per = base * 2 + altura * 2
area = base * altura
print("Perímetro:", per , "\narea:", area)
