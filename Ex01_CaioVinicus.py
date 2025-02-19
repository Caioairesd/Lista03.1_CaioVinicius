"""01 - Escreva um programa que forneça um tipo de aplicação financeira adequada a um investidor a partir de 2 dados fornecidos: 
O grau de aceitação de risco e o valor a ser investido. O grau de aceitação de risco deve ser lido no teclado na forma
de BX(baixo risco) ou AL(alto risco) se for fornecido algo diferente disto o programa deve mostrar uma mensagem indicando
que foi fornecido dado inválido. Para o valor ser deve ser um número real."""

GrauRisco = str(input("Digite qual grau de aceitação de risco você deseja:\nBX(baixo risco) ou AL(alto risco):").casefold())
Valor = float(input("Insira o valor que você deseja investir:"))


if Valor <1000 and GrauRisco == ('bx'):
    print("Um ivestimento de R$ {} e de baixo risco mais indicado é a poupança.".format(Valor))
elif Valor <1000 and GrauRisco == ('al'):
    print("Um ivestimento de R$ {} e de alto risco mais indicado são as criptomoedas Bitcoins.".format(Valor))
elif Valor >=1000 and GrauRisco == ('bx'):
    print("Um ivestimento de R$ {} e de baixo risco mais indicado é a renda fixa.".format(Valor))
elif Valor >=1000 and GrauRisco == ('al'):
    print("Um ivestimento de R$ {} e de alto risco mais indicado são as ações.".format(Valor))
elif GrauRisco != ('bx') or GrauRisco != ('al') or Valor <0 or Valor != float:
    print("Grau de risco ou valor inválido.")

                      
                      
print("---------------------------------------------------------------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")                      



