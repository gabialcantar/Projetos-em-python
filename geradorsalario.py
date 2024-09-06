#DIGITE SALARIO
salario= float(input("Digite o seu salário atual:"))

#DIGITE A PORCENTAGEM DO AUMENTO
p_aumento=float(input("Digite a porcentagem do aumento"))
aumento= salario*p_aumento/100

#NOVO SALARIO
novo_salario = salario + aumento
print("Um aumento de %5.2f %% em um salário de R$ %7.2f" % (p_aumento, salario))
print("é igual a um aumento de R$ %7.2f"% aumento)
print("Resultado em um novo salário de R$ %7.2f" % novo_salario)
