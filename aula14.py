salarioMensal = float(input("qual seu salario mensal "))

porcentagem =  float(input("qual seu reajuste em % "))

reajuste = salarioMensal * porcentagem / 100

calculo = salarioMensal + reajuste


print(f"o seu salario após o reajuste é: {calculo}")