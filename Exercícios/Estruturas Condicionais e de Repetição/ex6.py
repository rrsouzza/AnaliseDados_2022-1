num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
num3 = float(input("Insira outro número: "))
if (num1 > num2):
    if (num1 > num3):
        print("O maior número é ", num1)
    elif (num3 > num1):
        print("O maior número é ", num3)
elif (num2 > num3):
    print("O maior número é ", num2)
else:
    print("O maior número é ", num3)