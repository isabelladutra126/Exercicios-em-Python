import math
angulo = float(input("digite o valor em graus para um angulo: "))

graus = math.radians(angulo)

seno = math.sin(graus)
cosseno = math.cos(graus)
tangente = math.tan(graus)
print ("o seno deste angulo é: {:.2f}".format (seno))
print ("o cosseno deste angulo é: {:.2f} ".format (cosseno))
print ("a tangente deste angulo é: {:.2f} ".format (tangente))
