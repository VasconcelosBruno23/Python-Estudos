notas = [10.0, 7.8, 9.9, 6.5, 8.7, 9.2]
total = 0

for nota in notas:
    total += nota

print(f"A média de suas notas é: {total / len(notas)}")