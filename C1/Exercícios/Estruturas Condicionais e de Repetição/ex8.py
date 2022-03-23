produto1 = float(input("Insira o preço de um produto: "))
produto2 = float(input("Insira o preço de outro produto: "))
produto3 = float(input("Insira o preço de outro produto: "))
if (produto1 < produto2):
    if (produto1 < produto3):
        print("Você deve comprar o produto de R$", produto1)
    elif (produto3 < produto1):
        print("Você deve comprar o produto de R$", produto3)
elif (produto2 < produto3):
    print("Você deve comprar o produto de R$", produto2)
else:
    print("Você deve comprar o produto de R$", produto3)