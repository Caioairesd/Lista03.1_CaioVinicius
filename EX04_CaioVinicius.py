"""04 - No Senailândia mulheres e homens podem servir o exercício do País. O serviço é opcional e é muito comum que asa pessoas se 
apresentem para o serviço em algum momento da vida. Existe uma única restrição para o ingresso que é a idade da pessoa.
a) Para mulheres a idade aceita é entre 21 e 34 anos;
b) Para homens a idade aceita é entre 18 e 39 anos;
c) Escreva um programa que leia 3 dados de entrada: Nome, idade, gênero e informe se a pessoa será aceita ou não para o serviço.
Obs: Para o sexo deve ser lido Apenas uma caractere que pode ser (f ou F) e (m ou M) para feminino e masculino, qualquer coisa diferente deve 
imprimir inválido."""
nome = input("Insira seu nome:")
idade = int(input("Insira sua idade:"))
genero = input("Insira seu gênero\n(M ou m para masculino e F ou f para feminino)").lower()

if genero == 'f':
    if idade >= 21 and idade <= 34:
        print("{} você cumpre os requisitos para alistamento!".format(nome))
    else:
        print("{} você não cumpre os requisitos para o alistamento".format(nome))

elif genero == 'm':
    if idade >= 18 and idade <= 39:
        print("{} você cumpre os requisitos para alistamento!".format(nome))
    else:
        print("{} você não cumpre os requisitos para o alistamento".format(nome))

else:
    print("Dados inseridos inválidos.")







print("---------------------------------------------------------------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")   
