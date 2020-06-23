# 5. Escreva um programa que recebe uma letra e identifica se ela é consoante.

def consoante(letra):

    consoantes = "aeiou"

    if letra.lower() not in consoantes: # verificar se a letra digitada são consoantes

        print('Bem, se apareceu a palavra "True" é porque você digitou uma "CONSOANTE".')
        print('-' * 10)
        return True
    print('Bem, se apareceu a palavra "False" é porque você digitou uma "VOGAL".')
    print('-' * 10)
    return False

letra = input("Por Favor, digite aqui letra =>: ")

print(consoante(letra))
print('-' * 10)
print("Obrigado, por você ter participado desse teste.")