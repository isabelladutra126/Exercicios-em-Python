
água = float(input("Digite o valor da conta de água: R$"))
luz = float(input("Digite o valor da conta de luz: R$"))
telefone = float(input("Digite o valor da conta de seu telefone: R$"))
necessario = água + luz + telefone
salário = float(input("Digite o valor de seu salário: R$"))
falta = necessario - salário
if salário>necessario:
 print("Parabéns, seu salário é necessario para pagar as contas e ainda te resta R$ ", abs(falta))
elif salário==necessario:
 print("Ufa!! Você consegue pagar suas contas, porém não sobra nenhum centavo. :( ")
else:
 print("Infelizmente te falta r$ ", falta," para conseguir pagar suas contas. Você precisaria ganhar no mínimo r$ ", necessario, "para 
