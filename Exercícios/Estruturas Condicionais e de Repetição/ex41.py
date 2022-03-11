idades = []
for x in range(10):
  idades.append(int(input(str(x + 1) + " - Insira a idade: ")))

soma = 0
for x in idades:
  soma += x

media = soma / len(idades)

if media > 0 and media <= 25:
  print("Essa turma é jovem.")
elif media > 25 and media <= 60:
  print("Essa turma é adulta.")
elif media > 60:
  print("Essa turma é idosa.")

print("Média de idade da turma: " + str(media), sep='')