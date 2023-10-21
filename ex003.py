# Fazer um programa para ler o nome do aluno, ler 4 notas, ler faltas, calcular a média e imprimir
# OBS: Média > 7 = Aprovado; Faltas <= 5 = Aprovado

print("Aprovados 2023")

nome = str(input("Insira o nome do aluno e tecle ENTER "))

faltas = int(input("Insira o número total de faltas "))

n1 = float(input("Insira a primeira nota do aluno "))
n2 = float(input("Insira a segunda nota do aluno "))
n3 = float(input("Insira a terceira nota do aluno "))
n4 = float(input("Insira a quarta nota do aluno "))

media = (n1+n2+n3+n4)/4

if media >= 7 and faltas <= 5:
    status = str("Aprovado")
elif media >= 7 and faltas > 5:
    status = str("Reprovado por faltas")
elif media < 7 and faltas <= 5:
    status = str("Reprovado por média")
else:
    status = str("Reprovado")

print("Aluno:" , nome)
print("Faltas:" , faltas)
print("Média:" , media)
print(status)