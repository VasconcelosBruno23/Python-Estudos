produtos = []

produto1 = input("Informe o primeiro produto para adicioná-lo à lista: ")
produtos.append(produto1)

produto2 = input("Informe o segundo produto para adicioná-lo à lista: ")
produtos.append(produto2)

produto3 = input("Informe o terceiro produto para adicioná-lo à lista: ")
produtos.append(produto3)

buscaProduto = input("Digite qual o produto que você deseja verificar: ")

if buscaProduto in produtos:
    print(f"O produto {buscaProduto} está presente na lista.")
else:
    print(f"O produto {buscaProduto} não está na lista.")