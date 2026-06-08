soma = 0
valor = float(input("Digite um valor: "))

while valor != 0:
    soma += valor

    valor = float(input("Digite outro valor: "))

print(f"O resultado da soma de todos os valores digitados é de: {soma}")