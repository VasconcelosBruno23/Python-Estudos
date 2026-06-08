nota = float(input("Informe uma nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida, por favor insira uma outra nota.")

    nota = float(input("Informe uma nota: "))

print("Nota registrada com sucesso.")