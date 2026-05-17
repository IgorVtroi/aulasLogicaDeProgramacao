# Exercício 5
import random
while True:
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    resultado = n1 * n2
    print(f'Quanto é {n1} vezes {n2}?')
    resposta = int(input())
    if resposta == 0:
        print("fim do programa")
        break

    if resultado == resposta:
        print('ACERTOU!')
    else:
        print('ERROU!')
    continuar = str(input('Continuar? (S/N)\n'))
    if continuar != 'S' and continuar != 's':
        break