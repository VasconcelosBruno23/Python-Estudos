print("1 - Ver Saldo \n2 - Fazer depósito \n3 - Sacar \n0 - Sair")
opcao = input("Selecione uma das opções: ")

while opcao != "0":
    if opcao == "1":
        print("Seu saldo é de R$1000,00!")
    elif opcao == "2":
        print("Depósito selecionado!")
    elif opcao == "3":
        print("Saque selecionado!")
    else:
        print("Opção inválida.")

    print("\n\nO que você deseja fazer? \n1 - Ver Saldo \n2 - Fazer depósito \n3 - Sacar \n0 - Sair")
    opcao = input("Selecione outra opção: ")

print("Encerrando o sistema...")