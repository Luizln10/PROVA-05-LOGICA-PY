inicio = int(input("Insira um número do início:"))
fim = int(input("Insira um número do fim:"))

soma = 0
Pares = False

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma += numero
        Pares = True
if Pares:
    print(f"A soma dos pares é {soma}")
else: 
    print("Não tem números pares")
