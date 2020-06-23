# 12. Escreva uma função que liste todos os números primos até 258 (mais o dia do seu
# aniversário). Utilize a divisão modular (%).

# Números Primos, pelo “Crivo de Eratóstenes”:

def primonum (numero):
    primonum = True
    if(numero == 1):
        return False
    for i in range(2,numero):
        if(numero%i == 0):
            primonum = False
    if (primonum == True):
        return True
    else:
        return False

n = int(input("Bem, digite qualquer número até 258: "))
niver = int(input("Agora, digite o dia do seu aniversário: "))
soma = n + niver
print("A soma do dia do seu aniversário mais o número é igual:", soma)

for i in range(2,soma):
    if(primonum(i)):
         print(i)

print("Verifique acima a seguência a lista da somatória dos números primos.")