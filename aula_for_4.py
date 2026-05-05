
inicial = int(input("Digite o primeiro número da lista: "))
final = int(input("Digite o último número da lista: "))
divisivel = int(input("Digite um número para divisível: "))


if inicial <= final:
    for i in range(inicial, final + 1):
        if i % divisivel == 0:
            print(i, end=" ")
else:
    print("Lista inválida!")