# Atividade 002: Fazer um programa para ler a distância, valor do litro da gasolina, consumo do carro e calcular o gasto total

distance = float(input("Insira a distância a ser percorrida "))
gasolineCost = float(input("Insira o preço do litro da gasolina "))
carCost = float(input("Insira o consumo do carro por KM "))

totalUsed = float(distance/carCost)
totalCost = float(totalUsed*gasolineCost)

print("Total projetado: R$" , totalCost)