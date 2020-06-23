# 6. Escreva um programa que conte o número de letras de uma string e retorne e imprima o
# valor multiplicado por 10.

def contador():

    print()
    frase = input('Por favor, digite uma frase que iremos contar as letras:')
    print()

    print("Por favor, foi essa a frase que você digitou? ===>>", frase)
    print()

    print('-' * 90)
    print('Bem, a frase que você digitou mais os espços em branco tem comprimento de:', len(frase),'caracteres')
    print()

    print('Logo, o comprimento da frase vezes 10, ficou com um valor de:', len(frase) * 10,'caracteres')
    print('-' * 90)
    print()

    print('Obrigado por você ter participado dessa experimento!!!')

contador()

