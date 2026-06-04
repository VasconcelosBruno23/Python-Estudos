cont = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 10:
        break
    
    cont += 1

print(f"Você digitou {cont} números antes de adivinhar o número 10.")