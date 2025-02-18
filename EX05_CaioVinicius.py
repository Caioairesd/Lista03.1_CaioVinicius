"""05 - No comércio o conceito de margem bruta é uma 5 que é aplicada ao preço de custo para se obter o preço de venda. 
Uma loja tem como política comercial, aplicar uma margem bruta de 45% quando o preço bruto é <= 100 reais 
e o produto custa > 100 a margem bruta é de 35% . Escreva um programa que leia o preço  do produto e mostre o seu custo."""

preco = int(input("Insira o valor do produto:"))

if preco > 100:
    margem = preco * 35/100
    print("A margem bruta do preço é {}".format(margem))
else:
    margem = preco * 45/100
    print("A margem bruta do preço é {}".format(margem))