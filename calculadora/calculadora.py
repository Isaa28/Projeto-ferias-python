op = input("Qual a operação que você deseja(*,-,+,/):")
n1 = int(input("Digite um número para realizar uma operação:"))
n2 = int(input("Digite o segundo número para a operação:"))
mult = "*"
sam = "+"
sub = "-"
div = "/"
if op == mult:
    res = n1 * n2
if op == sam:
    res = n1 + n2
if op == sub:
    res = n1 - n2
if op == div:
    res = n1 / n2
print(f"O resultado da sua operação é {res}")