print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
s = input("Digite sua senha : ")
while s.islower():
        s = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")

while len(s) < 7 :
    s = input("A senha deve ter pelo menos 8 caracteres: ")

while s.isalpha() :
    s = input("Necessita de um numero: ")

while s.isalnum() :
    s = input("Necessita de um Caractere especial: ")
print("Sua senha é válida.")