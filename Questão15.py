PI = 3.14
raio = input("Digite o valor do raio")
raio = raio.replace(",",".")
raio = float(raio)
per = 2 * PI * raio
area = PI * raio ** 2
print("Perímetro do círculo:", per, "\nÁrea do círculo:", area)
