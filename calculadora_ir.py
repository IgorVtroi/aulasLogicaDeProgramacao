class calculadora_ir():
    print("---calculadora de imposto de renda 2026---")

    escolha = int(input("deseja saber os valores: \n1 - mensais \n2 - anuais? \n(1/2):"))

    if escolha == 1:
        renda = float(input("qual é o valor da sua renda mensal? (xxx.xx)\nR$:"))

        if renda <= 2428.80:
            aliquota = 0
            deducao = 0
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - 312.89)
            print(f"com sua renda de R${renda:.2f}, você está isento\nimposto final R${imposto_final:.2f}")

        elif renda <= 2826.65:
            aliquota = 0.075
            deducao = 182.16
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - 312.89)
            print(f"salario R${renda:.2f}\ndeducao R${deducao:.2f}\naliquota {aliquota:.3f}\nimposto bruto R${imposto_bruto:.2f}")
            print(f"com sua renda de R${renda:.2f} você pagará R${imposto_final:.2f}\ne sobrará R${renda - imposto_final:.2f}")

        elif renda <= 3751.05:
            aliquota = 0.15
            deducao = 394.16
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - 312.89)
            print(f"salario R${renda:.2f}\naliquota {aliquota:.2f}\ndeducao R${deducao:.2f}\nimposto bruto R${imposto_bruto:.2f}")
            print(f"com sua renda de R${renda:.2f} você pagará R${imposto_final:.2f}\ne sobrará R${renda - imposto_final:.2f}")

        elif renda <= 4664.68:
            aliquota = 0.225
            deducao = 675.49
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - 312.89)
            print(f"salario R${renda:.2f}\ndeducao R${deducao:.2f}\naliquota {aliquota:.3f}\nimposto bruto R${imposto_bruto:.2f}")
            print(f"com sua renda de R${renda:.2f} você pagará R${imposto_final:.2f}\ne sobrará R${renda - imposto_final:.2f}")

        elif renda <= 5000.00:
            aliquota = 0.275
            deducao = 908.73
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - 312.89)
            print(f"salario R${renda:.2f}\ndeducao R${deducao:.2f}\naliquota {aliquota:.3f}\nimposto bruto R${imposto_bruto:.2f}")
            print(f"com sua renda de R${renda:.2f} você pagará R${imposto_final:.2f}\ne sobrará R${renda - imposto_final:.2f}")

        elif renda <= 7350.00:
            aliquota = 0.275
            deducao = 908.73
            reducao = 978.62 - (0.133145 * renda)   # fórmula da tabela de redução
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - reducao)
            print(f"salario R${renda:.2f}\ndeducao R${deducao:.2f}\naliquota {aliquota:.3f}\nreducao R${reducao:.2f}\nimposto bruto R${imposto_bruto:.2f}")
            print(f"com sua renda de R${renda:.2f} você pagará R${imposto_final:.2f}\ne sobrará R${renda - imposto_final:.2f}")

        else:
            aliquota = 0.275
            deducao = 908.73
            reducao = 0
            imposto_bruto = renda * aliquota - deducao
            imposto_final = max(0, imposto_bruto - reducao)
            print(f"salario R${renda:.2f}\ndeducao R${deducao:.2f}\naliquota {aliquota:.3f}\nimposto bruto R${imposto_bruto:.2f}")
            print(f"com sua renda de R${renda:.2f} você pagará R${imposto_final:.2f}\ne sobrará R${renda - imposto_final:.2f}")

    elif escolha == 2:
        renda_anual = float(input("qual é o valor da sua renda anual? (xxxxx.xx)\nR$:"))
        renda = renda_anual / 12  # converte para mensal para calcular

        print(f"\n--- cálculo anual (baseado em renda mensal de R${renda:.2f}) ---")

        if renda <= 2428.80:
            imposto_mensal = 0.0
        elif renda <= 2826.65:
            imposto_mensal = max(0, renda * 0.075 - 182.16 - 312.89)
        elif renda <= 3751.05:
            imposto_mensal = max(0, renda * 0.15 - 394.16 - 312.89)
        elif renda <= 4664.68:
            imposto_mensal = max(0, renda * 0.225 - 675.49 - 312.89)
        elif renda <= 5000.00:
            imposto_mensal = max(0, renda * 0.275 - 908.73 - 312.89)
        elif renda <= 7350.00:
            reducao = 978.62 - (0.133145 * renda)
            imposto_mensal = max(0, renda * 0.275 - 908.73 - reducao)
        else:
            imposto_mensal = max(0, renda * 0.275 - 908.73)

        imposto_anual = imposto_mensal * 12
        liquido_anual = renda_anual - imposto_anual

        print(f"renda anual bruta: R${renda_anual:.2f}")
        print(f"imposto mensal estimado: R${imposto_mensal:.2f}")
        print(f"imposto anual total: R${imposto_anual:.2f}")
        print(f"renda anual líquida: R${liquido_anual:.2f}")

    else:
        print("opção inválida. escolha 1 ou 2.")


calculadora_ir()