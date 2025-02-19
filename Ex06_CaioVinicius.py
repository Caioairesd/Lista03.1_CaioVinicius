"""06 - Nas eleições municipais, os municípios com 200000 eleitores ou mais tem segundo turno caso o primeiro colocado não tenha mais que 50%.
Escreva um programa que leia o nome do município, a qtde. de eleitores a qtde. de votos do candidato mais votado e informe se haverá 2° turno ou não"""


municipio = input("Insira o nome do município:")
eleitores = float(input("Insira a quantidade de eleitores:"))
votos = float(input("Insira a quantidade de votos do candidato mais votado:"))

aliquota = eleitores * 50/100

if eleitores < 200000:
    print("{} não pode ter segundo turno devido quantidade de eleitores.".format(municipio))

elif votos > aliquota:
    print("Não haverá segundo turno no município de {}".format(municipio))

else:
    print("Haverá segundo turno no município de {}".format(municipio))





print("---------------------------------------------------------------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")   