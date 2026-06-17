produtos = []

produto = input("Digite um produto para armazená-lo na lista: ")

while produto != "sair":
    produtos.append(produto)
    produto = input("Digite um produto para armazená-lo na lista: ")

print(f"Segue a lista completa: {produtos}")
print("Finalizando o sistema...")