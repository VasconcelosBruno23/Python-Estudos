cont = 0
senha = input("Digite a sua senha: ")

while senha != "python123":
    print("Senha incorreta, tente novamente!")
    cont += 1

    senha = input("Digite sua senha novamente: ")

print("Senha correta, seja bem-vindo!")
print(f"Você errou a senha {cont} vezes antes de acertar.")