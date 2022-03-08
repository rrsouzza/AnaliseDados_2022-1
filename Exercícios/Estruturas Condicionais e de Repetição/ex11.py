salarioAtual = float(input("Insira o valor do seu salário atual:"))
if salarioAtual <= 280:
  percentualAumento = 20
elif salarioAtual > 280 and salarioAtual <= 700:
  percentualAumento = 15
elif salarioAtual > 700 and salarioAtual <= 1500:
  percentualAumento = 10
elif salarioAtual > 1500:
  percentualAumento = 5
else:
  print("Ocorreu um erro.")

valorAumento = (salarioAtual / 100) * percentualAumento
salarioReajustado = salarioAtual + valorAumento

print("Salário antes do reajuste: R$", salarioAtual)
print("Percentual de aumento aplicado: ", percentualAumento)
print("Valor do aumento: R$", valorAumento)
print("Novo salário após o aumento: R$", salarioReajustado)