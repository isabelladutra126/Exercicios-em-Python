
valorcompra = float(input("Digite o valor da compra: R$"))
if valorcompra > 200:
 desconto = 0.20 * valorcompra
 valorcdesconto = valorcompra - desconto
 print(f"O valor da compra com desconto é: R${valorcdesconto:.2f}")
else:
 print(f"O valor da compra é: R${valorcompra:.2f}")