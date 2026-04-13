#Peça um número ao usuário.
while True:
    num = float(input("digite o numero da taboada que deseja saber (1 até 10): "))
    # Mostre a tabuada deste número.
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

 # Pergunte se o usuário deseja exibir outra tabuada.
    resposta = input("digite S ou sim para continuar: ")
    if resposta.lower() not in ("s", "sim"):
        break




# Se ele digitar "S" (ou "sim"), receba um novo número e repita o processo.
# O programa deve encerrar apenas quando o usuário responder que não deseja mais
#continuar.