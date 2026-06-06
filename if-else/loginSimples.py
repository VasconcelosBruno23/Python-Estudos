usuario = input("Informe o seu usuário: ")
senha = input("Digite a sua senha: ")

if usuario == "admin" and senha == "1234":
    print("Login efetuado com sucesso!")
else:
    print("Usuário ou senha inválidos.")