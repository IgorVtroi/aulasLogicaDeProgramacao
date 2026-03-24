dia = int(input("quantos dias"))
hora = int(input("quantas horas"))
minutos = int(input("quantos minutos"))
segundos = int(input("quantos segundos"))

total = segundos + minutos * 60 + hora * 60 * 60 + dia * 60 * 60

print(total)

