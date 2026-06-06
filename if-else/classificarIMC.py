peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
elif imc < 30:
    print("Você está em estado de sobrepeso.")
else:
    print("Você está obeso.")