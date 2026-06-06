num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Selecione um operador (+, -, * ou /): ")

if operador == "+": 
    soma = num1 + num2
    print(f"{num1} + {num2} = {soma}")

elif operador == "-":
    subtracao = num1 - num2
    print(f"{num1} - {num2} = {subtracao}")

elif operador == "*":
    multiplicacao = num1 * num2
    print(f"{num1} * {num2} = {multiplicacao}")

elif operador == "/":
    divisao = num1 / num2
    print(f"{num1} / {num2} = {divisao}")
    
else:
    print("Selecione um operador válido.")