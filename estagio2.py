import xml.etree.ElementTree as ET

vetor = []

for i in range(30):
  vetor.append(input("Digite o valor de faturamento do dia: "))
menor = float(vetor[0])

for i in range(1,30):
  if float(vetor[i]) < menor:
    menor = float(vetor[i])

maior = float(vetor[0])

for i in range(1,30):
  if float(vetor[i]) > maior:
    maior = float(vetor[i])

soma = float(0)

for i in range(30):
  soma += float(vetor[i])

media = soma / 30
acima = 0

for iontinue in range(30):
  if float(vetor[i]) > media:
    acima += 1

dados = ET.Element("dados")

menor_valor = ET.SubElement(dados, "menor_valor")
menor_valor.text = str(menor)

maior_valor = ET.SubElement(dados, "maior_valor")
maior_valor.text = str(maior)

dias_acima_media = ET.SubElement(dados, "dias_acima_media")
dias_acima_media.text = str(acima)

arvore = ET.ElementTree(dados)
arvore.write("dados.xml")

print("Menor valor: " + dados[0].text)
print("Maior valor: " + dados[1].text)
print("Dias acima da média: " + dados[2].text)
