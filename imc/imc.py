M = float(input("Digite sua massa(em kg):"))
A = float(input("Digite sua altura(em metros):"))
imc = M / (A * A)
IMC = round(imc,2)
print(f"seu imc é {IMC}.")
if IMC < 18.5:
    print("Você está abaixo do peso.")
if IMC >= 18.5 and IMC< 25:
    print("Você está com peso normal.")
if IMC >= 25 and IMC < 30:
    print("Você está acima do peso.")
if IMC >= 30 and IMC < 35:
    print("Você está sobrepeso.")
if IMC >= 35:
    print ("Você está obeso.")