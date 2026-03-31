pergunta = int(input("qual volume deseja saber? \n- 1 lata de oleo \n- 2 caixa de papelão: "))

if pergunta == 1:
    raio = float(input("qual o raio da lata de ole: (cm) "))
    altura = float(input("qual a altura da oleo? (cm) "))
    volume = 3.14159 * raio**2 * altura
    print(f"o volume da lata de oleo é de  {volume} cm³")
else:
    altura = float(input("qual a altura da caixa de papelão? (cm)"))
    largura = float(input("qual a largura da caixa do papelão (cm)"))
    comprimento = float(input("qual o comprimento da caixa (cm)"))
    resultado = altura * largura * comprimento
    print(f"o volume da caixa de paeplão é cm³ {resultado}")







#if volume = 3.14159 * raio**2 * altura

#if pergunta == "1":


