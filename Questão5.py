salario = input("Digite o seu salario ")
salario = salario.replace(",",".")
salario = float(salario)
aumento = input("Digite o percentual de aumento (Apenas números) ")
aumento = int(aumento)
aumento = aumento / 100
saln = salario + salario * aumento
print("O novo salário é: R$", saln, "com um aumento de:", aumento * 100, "%")
