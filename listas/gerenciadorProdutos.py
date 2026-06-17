produtos = []

print("1 - Adicionar produto \n2 - Remover produto \n3 - Ver produtos \n4 - Buscar produto \n0 - Sair")
opcao = input("Selecione uma das opções: ")

while opcao != "0":
    if opcao == "1":
        adicionarProduto = input("Insira um produto para adicioná-lo à lista: ")
        produtos.append(adicionarProduto)

    elif opcao == "2":
        removerProduto = input("Informe um produto existente para removê-lo da lista: ")
        if removerProduto in produtos:
            produtos.remove(removerProduto)
            print(f"O produto {removerProduto} foi removido.")
        else:
            print(f"O produto {removerProduto} não existe.")

    elif opcao == "3":
        print(f"A lista de produtos se encontra atualmente assim: {produtos}")

    elif opcao == "4":
        buscarProduto = input("Informe um produto para verificar se está presente na lista: ")
        if buscarProduto in produtos:
            print(f"O produto {buscarProduto} está na lista.")
        else:
            print(f"O produto {buscarProduto} não está na lista.")

    else:
        print("Opção inválida.")

    print("\n1 - Adicionar produto \n2 - Remover produto \n3 - Ver produtos \n4 - Buscar produto \n0 - Sair")
    opcao = input("Selecione uma das opções: ")

print("Encerrando o sistema...")