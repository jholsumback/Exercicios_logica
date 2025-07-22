#Solicita o número para o usuário
Numero = int(input("Digite um número: "))

#Função veirifica se é par ou impar
def Parouimpar(Numero):
    if Numero % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"

#Chama a função
R = Parouimpar(Numero)

print(f"O número {Numero} é um valor {R}")
