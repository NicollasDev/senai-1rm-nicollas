from colorsys import *
nota1 = float( input("informe primeira nota: "))
nota2 = float( input("informe segunda nota: "))
nota3 = float( input("informe terceira nota: "))
media = (nota1 + nota2 + nota3) /3
if media >= 6:
    print("Sua média foi {:.1f}. Aprovado!".format(media))
elif media >= 5:
    print("Sua média foi {:.1f}. Conselho de classe!".format(media))
else:
    print("Sua média foi {:.1f}. Reprovado!".format(media))

