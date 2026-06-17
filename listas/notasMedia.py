notas = []

nota = float(input("Informe as suas notas: "))

while nota != -1:
    notas.append(nota)
    print("Digite -1 caso queira encerrar o sistema.")
    nota = float(input("Informe as suas notas: "))

if len(notas) > 0:
    print(f"Aqui está a sua lista de notas: {notas}")
    print(f"Quantidade de notas inseridas: {len(notas)}")
    print(f"A sua média de notas: {sum(notas) / len(notas)}")
else:
    print("Nenhuma nota foi inserida.")

print("Encerrando o sistema...")