valorprestacao = float(input("digite o valor de sua prestação: "))
multa = float(input("digite a porcentagem de multa pelo atraso: "))
qtdedias = float(input("digite a quantidade de dias de atraso: "))

prestacao = valorprestacao+(valorprestacao*(multa/100)*qtdedias)
print ("o valor da sua prestação em atraso ficara no total de R$  ", prestacao)
