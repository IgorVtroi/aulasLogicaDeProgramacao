import random

numeros = [random.randint(1, 50) for _ in range(20)]

print("Vetor gerado:")
print(numeros)

multiplos_de_5 = [n for n in numeros if n % 5 == 0]

if multiplos_de_5:
    print(f"\nMúltiplos de 5: {multiplos_de_5}")
else:
    print("\nNenhum múltiplo de 5 encontrado.")