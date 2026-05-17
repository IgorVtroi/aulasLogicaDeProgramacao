import random as rd

vetor = []

# cria os 10 números aleatórios
for i in range(10):
    numero = rd.randint(1, 50)
    vetor.append(numero)

pares = 0
impares = 0

# percorre os valores da lista
for numero in vetor:

    if numero % 2 == 0:
        print(f"{numero} é par")
        pares = pares + 1

    else:
        print(f"{numero} é ímpar")
        impares = impares + 1

print("\nVetor:", vetor)
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")