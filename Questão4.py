valor = input("Digite o preço da compra ")
valor = valor.replace(",",".")
valor = float(valor)
desc = input("Digite o percentual de desconto (Apenas números) ")
desc = int(desc)
desc = desc / 100
valdesconto = valor - valor * desc
print("Preço final: R$" , valdesconto, "com desconto de:", desc * 100, "%")
