nome = input("Informe o seu nome: ")
media = float(input("Informe a sua média: "))
frequencia = float(input("Informe a sua frequência: "))

if media >= 6 and frequencia >= 75:
    print(f"{nome}, você foi aprovado!")
elif media >= 6 and frequencia < 75:
    print(f"{nome}, você foi reprovado por faltas!")
elif media < 6 and frequencia >= 75:
    print(f"{nome}, você foi reprovado por notas!")
else:
    print(f"{nome}, você foi reprovado!")