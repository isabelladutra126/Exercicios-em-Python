turno1 = 1
turno2 = 2 

print ("Para turno da manhã, digite 1. Para turno da noite, digite 2.")
turno=  int(input("Digite seu turno:"))
horario = int(input("Digite a quantidade de horas trabalhadas no turno: "))

if turno == turno1:
    salario = horario * 37,50
    print ("Seu salário sera de R$ ", salario)
else:
    salario = horario * 45,00
    print ("Seu salário sera de R$ ", salario)



