valorHora = float(input("Insira o valor da sua hora trabalhada:"));
qtdHoras = float(input("Insira a quantidade de horas trabalhadas:"));
salarioBruto = valorHora * qtdHoras;

if salarioBruto <= 900:
  taxaIR = 0;
  descontoIR = 0;
elif salarioBruto > 900 and salarioBruto <= 1500:
  taxaIR = 5;
  descontoIR = (salarioBruto / 100) * taxaIR;
elif salarioBruto > 1500 and salarioBruto <= 2500:
  taxaIR = 10;
  descontoIR = (salarioBruto / 100) * taxaIR;
elif salarioBruto > 2500:
  taxaIR = 20;
  descontoIR = (salarioBruto / 100) * taxaIR;
else:
  print("Ocorreu um erro.");

descontoINSS = (salarioBruto / 100) * 10;
fgts = (salarioBruto / 100) * 11;
totalDescontos = descontoIR + descontoINSS;
salarioLiquido = salarioBruto - totalDescontos;

print("Salário Bruto: (", valorHora, " * ", qtdHoras, ") : R$", salarioBruto);
print("IR (", taxaIR, "%) : R$", descontoIR);
print("INSS (10%) : R$", fgts);
print("Total de descontos: R$", totalDescontos);
print("Salário Líquido : R$", salarioLiquido);