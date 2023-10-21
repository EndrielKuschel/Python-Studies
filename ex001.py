# Atividade 001: Fazer um programa para ler o nome do aluno, ler 4 notas, calcular a média e imprimir

print("Cálculo de média")

nome = str(input("Insira o nome do aluno e tecle ENTER "))

n1 = float(input("Insira a primeira nota do aluno "))
n2 = float(input("Insira a segunda nota do aluno "))
n3 = float(input("Insira a terceira nota do aluno "))
n4 = float(input("Insira a quarta nota do aluno "))

media = (n1+n2+n3+n4)/4

print(nome , media) 
