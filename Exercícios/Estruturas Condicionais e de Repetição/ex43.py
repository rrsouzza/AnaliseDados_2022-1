from ast import Num

class Cidade(object):
  def __init__(self, codigo, numVeiculosPasseio, numAcidentes):
    self.codigo = codigo
    self.numVeiculosPasseio = numVeiculosPasseio
    self.numAcidentes = numAcidentes

cidades = []

qtdCidades = int(input("Quantas cidades gostaria de registrar? "))
for x in range(qtdCidades):
  codigo = len(cidades) + 1
  qtdVeiculosPasseio = int(input("Quantos veículos de passeio essa cidade possui? "))
  qtdAcidentes = int(input("Quantos acidentes ocorreram nessa cidade? "))

  cidadeNova = Cidade(str(codigo), qtdVeiculosPasseio, qtdAcidentes)
  cidades.append(cidadeNova)

# cidade1 = Cidade("01", 1500, 120)
# cidade2 = Cidade("02", 45000, 1450)
# cidade3 = Cidade("03", 280, 15)
# cidade4 = Cidade("04", 62300, 8000)
# cidade5 = Cidade("05", 165750, 49240)
# cidades = [cidade1, cidade2, cidade3, cidade4, cidade5]

maiorIndiceAcidentes = 0
cidadeMaiorIndiceAcidentes = ""
menorIndiceAcidentes = 99999
cidadeMenorIndiceAcidentes = ""
somaVeiculos = 0
somaAcidentesCidadesMenosDoisMilVeiculos = 0
qtdCidadesMenosDoisMilVeiculos = 0

for x in range(len(cidades)):
  if cidades[x].numAcidentes > maiorIndiceAcidentes:
    maiorIndiceAcidentes = cidades[x].numAcidentes
    cidadeMaiorIndiceAcidentes = cidades[x].codigo

  if cidades[x].numAcidentes < menorIndiceAcidentes:
    menorIndiceAcidentes = cidades[x].numAcidentes
    cidadeMenorIndiceAcidentes = cidades[x].codigo

  somaVeiculos += cidades[x].numVeiculosPasseio

  if cidades[x].numVeiculosPasseio < 2000:
    somaAcidentesCidadesMenosDoisMilVeiculos += cidades[x].numAcidentes
    qtdCidadesMenosDoisMilVeiculos += 1

mediaVeiculosCidades = somaVeiculos / len(cidades)
mediaAcidentesCidadesMenosDoisMil = somaAcidentesCidadesMenosDoisMilVeiculos / qtdCidadesMenosDoisMilVeiculos

print("A cidade " + str(cidadeMaiorIndiceAcidentes) + " é a cidade com maior índice de acidentes, com " + str(maiorIndiceAcidentes) + " acidentes registrados.", sep='')
print("A cidade " + str(cidadeMenorIndiceAcidentes) + " é a cidade com menor índice de acidentes, com " + str(menorIndiceAcidentes) + " acidentes registrados.", sep='')
print("A média de veículos nas cidades são de " + str(round(mediaVeiculosCidades, 2)) + " veículos.", sep='')
print("A média de acidentes nas cidades com menos de 2000 veículos de passeio é de " + str(mediaAcidentesCidadesMenosDoisMil) + " acidentes.", sep='')