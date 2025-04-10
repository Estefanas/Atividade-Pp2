valor = input("Informe o valor do produto ")
valor = valor.replace(",",".")
valor = float(valor)
qtd = input("Informe a quantidade do produto ")
qtd = int(qtd)
valortotal = valor * qtd
float(valortotal)
print("O valor da compra deu R$", valortotal)
