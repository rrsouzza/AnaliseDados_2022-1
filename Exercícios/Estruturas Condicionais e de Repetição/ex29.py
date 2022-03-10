validado = False
while validado == False:
  usuario = input("Insira o nome de usuário: ")
  senha = input("Insira a senha: ")
  validado = True if senha != usuario else False
  print("A senha não pode ser igual ao usuário! ") if validado == False else None