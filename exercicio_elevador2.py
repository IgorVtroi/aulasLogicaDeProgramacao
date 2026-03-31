capcidadeMax = 500
p1 = int(input("Digiteo peso do passageiro 1: "))
p2 = int(input("Digiteo peso do passageiro 2: "))
p3 = int(input("Digiteo peso do passageiro 3: "))
p4 = int(input("Digiteo peso do passageiro 4: "))
p5 = int(input("Digiteo peso do passageiro 5: "))

if p1 + p2 + p3 + p4 + p5 > capcidadeMax:
    print("o peso total de passageiros excede o limíte máximo do elevador")
else:
    print("o peso total dos passageiros está dentro do limite do elevador")
