nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
if (((nota1 + nota2) / 2) == 10):
    print("Aprovado com distinção.")
elif (((nota1 + nota2) / 2) >= 7):
    print("Aprovado.")
else:
    print("Reprovado.")