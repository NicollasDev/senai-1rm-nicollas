salario = float( input("Informe seu salário professor do senai: "))
if salario <= 8250:
    reajuste = salario * 1.15
else:
    reajuste = salario * 1.10
print("seu salário de R${} reais foi para R${:.2f} reais".format(salario, reajuste))
