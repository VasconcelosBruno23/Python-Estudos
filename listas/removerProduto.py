produtos = []

produto1 = input("Informe o primeiro produto para adicioná-lo à lista: ")
produtos.append(produto1)

produto2 = input("Informe o segundo produto para adicioná-lo à lista: ")
produtos.append(produto2)

produto3 = input("Informe o terceiro produto para adicioná-lo à lista: ")
produtos.append(produto3)

print(f"Aqui está a sua lista de produtos: {produtos}")

removerProduto = input("Insira um produto existente para removê-lo da lista: ")
produtos.remove(removerProduto)

print(f"A lista atualizada é: {produtos}")