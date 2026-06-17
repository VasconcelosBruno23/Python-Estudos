notas = []

nota = float(input("Informe as suas notas: "))

while nota != -1:
    notas.append(nota)
    print("Digite -1 caso queira encerrar o sistema.")
    nota = float(input("Informe as suas notas: "))

if len(notas) > 0:
    print(f"Sua lista de notas: {notas}")
    print(f"A maior nota da sua lista é: {max(notas)}")
    print(f"A menor nota da sua lista é: {min(notas)}")
else:
    print("Nenhuma nota foi inserida.")

print("Encerrando o sistema...")