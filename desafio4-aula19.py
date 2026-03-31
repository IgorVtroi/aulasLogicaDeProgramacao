op = int(input("-(1) para area do retalgulo \n-(2) para area do triangulo \n: "))

if op == 1:
    base = float(input("qual o valor da base do retangulo: "))
    altura = float(input("qual a autura do retangulo: "))
    area = base * altura
    print(f"o valor da area do retangulo: {area}")
else:
    base = float(input("qual a base do triangulo: "))
    altura = float(input("qual a altura do triangulo: "))
    area =  base * altura / 2
    print(f"o valor da area do triangulo: {area}")