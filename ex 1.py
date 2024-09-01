h = float(input("digite a altura do tronco da pirâmide em cm: "))
bmenor = float(input("digite o valor da base menor em cm: "))
bmaior = float(input("digite o valor da base maior em cm: "))

volume = h/3 * (bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)
print ("o volume do  tronco da piramide é de {:.2f} cm²" .format (volume))

