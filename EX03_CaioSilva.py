"""03 - Uma empresa financeira concede empréstimos a pessoas física quando o valor da parcela é menor que 8% do salário da pessoa.
Escreva um programa que leia 2 números reais. Valor do salário  e o valor da parcela e se o empréstimo será concedido ou não."""

parcela = float(input("Qual o valor da parcela que você deseja pagar?"))
salário = float(input("Qual o do seu salário?"))

aliquota = 8/100
condicao = salário * aliquota

if parcela < condicao:
    print("O empréstimo pode ser concedido!")
else:
    print("Empréstimo recusado!")



print("---------------------------------------------------------------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")   