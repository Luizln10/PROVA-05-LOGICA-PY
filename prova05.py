alunos = int(input("Digite o número dos alunos:"))

somaFinal = 0

for numero in range(alunos):
    nome = input("Digite o nome do aluno:")
    nota1 = float(input("Digite a nota 1:"))
    nota2 = float(input("Digite a nota 2:"))
    nota3 = float(input("Digite a nota 3:"))
    media = (nota1 + nota2 + nota3)/3

    somaFinal += media

    if media >= 7:
        print("Você está aprovado!")
    else:
        print("Você está reprovado!")
    
    print(f"Nome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media}")
    mediaFinal = somaFinal / alunos
    print(f"Média geral: {mediaFinal}")
