import random

numeros = [random.randint(1, 50) for _ in range(20)]

print("Vetor gerado:")
print(numeros)

pares = [n for n in numeros if n % 2 == 0]

if pares:
    media_pares = sum(pares) / len(pares)
    print(f"\nNúmeros pares: {pares}")
    print(f"Média dos pares: {media_pares:.2f}")
else:
    print("\nNenhum número par encontrado.")E