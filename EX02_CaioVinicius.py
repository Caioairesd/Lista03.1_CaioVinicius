"""02 - Escreva um programa para exibir na tela o nome e a categoria, o programa deve ler o String para o nome e um 
número real para o peso. Conforme o peso ocorrerá o enquadramento na categoria"""

nome = input("Qual o nome do atleta:").title()
peso = float(input("Qual o peso do atleta:"))

if peso < 52:
    categoria = 'inválida'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >= 52 and  peso < 65:
    categoria = 'pena'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >= 65  and peso < 72:
    categoria = 'leve'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >= 72 and peso < 79:
    categoria = 'ligeiro'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >= 79 and peso < 86:
    categoria = 'meio médio'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >= 86 and peso < 90:
    categoria = 'médio'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >= 90  and peso < 100:
    categoria = 'meio pesado'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))

elif peso >100:
    categoria = 'pesado'
    print("A categoria para o(a) atleta {} de {} KG é {}".format(nome,peso,categoria))





print("---------------------------------------------------------------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")                      
