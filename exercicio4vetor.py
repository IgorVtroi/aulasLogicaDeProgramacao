import random

numeros = [random.randint(1, 50) for _ in range(20)]

print("Vetor gerado:")
print(numeros)

divisor = int(input("\nDigite um número para encontrar os múltiplos: "))

multiplos = [n for n in numeros if n % divisor == 0]

if multiplos:
    print(f"\nMúltiplos de {divisor}: {multiplos}")
else:
    print(f"\nNenhum múltiplo de {divisor} encontrado.")