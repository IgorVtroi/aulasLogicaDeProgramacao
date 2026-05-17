import random

opcao = int(input("Digite uma opção (1 - ordem normal / 2 - ordem inversa): "))

numeros = [random.randint(1, 50) for _ in range(10)]

print("\nVetor gerado:")
print(numeros)

if opcao == 1:
    print("\nVetor em ordem normal:")
    for i in range(len(numeros)):
        print(numeros[i], end=" ")

elif opcao == 2:
    print("\nVetor em ordem inversa:")
    for i in range(len(numeros) - 1, -1, -1):
        print(numeros[i], end=" ")

else:
    print("\nOpção inválida.")