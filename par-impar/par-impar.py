n = int(input("Digite um número para saber se ele é par ou ímpar:"))
res = n % 2
if res == 0 :
    res = "Esse é um número par!"
else :
    res = "Esse é um número ímpar!"
print(f"{res}")