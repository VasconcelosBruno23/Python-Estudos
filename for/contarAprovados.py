notas = [4.8, 7.2, 10.0, 9.6, 5.9, 6.1, 5.1, 2.3]
aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1

print(f"Quantidade de alunos: {len(notas)}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")