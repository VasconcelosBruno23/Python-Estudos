print("1 - Ver Saldo \n2 - Depositar \n3 - Sacar \n0 - Sair")
opcao = input("Selecione uma das opções: ")
saldo = 1000

while opcao != "0":
    if opcao == "1":
        print(f"O seu saldo atual é: {saldo}")
    elif opcao == "2":
        deposito = float(input("Digite um valor para realizar o depósito: R$"))
        saldo += deposito
        print(f"O valor depositado foi de R${deposito}, o seu saldo atual é: {saldo + deposito}")
    elif opcao == "3":
        saque = float(input("Digite um valor para realizar o saque: R$"))
        saldo -= saque
        print(f"O valor retirado foi de R${saque}, o seu saldo atual é: {saldo - saque}")
    else:
        print("Opção inválida, por favor selecione uma opção novamente.")

    print("\n\nO que você deseja fazer? \n1 - Ver Saldo \n2 - Depositar \n3 - Sacar \n0 - Sair")
    opcao = input("Selecione uma das opções: ")

print("Encerrando o sistema...")