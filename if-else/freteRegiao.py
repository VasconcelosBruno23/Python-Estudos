regiao = input("Informe a região de entrega (sul, sudeste, centro-oeste, nordeste ou norte): ")

if regiao == "sul":
    print("O frete é: R$20,00")
elif regiao == "sudeste":
    print("O frete é: R$25,00")
elif regiao == "centro-oeste":
    print("O frete é: R$30,00")
elif regiao == "nordeste":
    print("O frete é: R$35,00")
elif regiao == "norte":
    print("O frete é: R$40,00")
else:
    print("Região inválida.")