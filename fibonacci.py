lim =  int(input("digite limite: "))
n1 = 1
n2 = 1
print(n1)
print(n2)
if lim <= 2:
   print()
else:
    for i in range(3, lim + 1, 1):
        result =  n1 + n2
        print(f"{result}")
        n1 = n2
        n2 = result
