a = int(input ("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a > b and b < c:
    print("O menor valor é b")
elif c < a and c < b:
    print("O menor valor é c")
else: 
    print ("O menor valor é a")