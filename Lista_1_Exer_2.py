# 2. Altere o programa acima para que o usuário possa entrar com o número máximo de estrelas.

def triangulo(n):

    return "\n".join([" " * (n - i) + "*" * (i + i - 1)
    for i in range(1, n + 1)])

print('Olá! Qual é o seu nome?')
meuNome = input()

numero = int(input("Olá, qual é a quantidade de linhas que você quer no seu triangulo: "))

print (triangulo(numero))

print()
print(meuNome + "<=== PARABÉNS!!! Veja acima o triangulo que você criou ... ")

