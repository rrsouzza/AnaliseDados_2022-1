letra = input("Insira uma letra: ")
if (letra[0].upper() == "A" or
    letra[0].upper() == "E" or
    letra[0].upper() == "I" or
    letra[0].upper() == "O" or
    letra[0].upper() == "U"):
    print("Você inseriu uma vogal.")
else:
    print("Você inseriu uma consoante.")