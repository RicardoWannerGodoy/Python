# 3. Escreva um programa que corre os números de 23 a 83 e imprime. Mas, quando for múltiplo
# de três, imprima ‘Pum’, quando for múltiplo de 5 imprima ‘Bla’, quando for de ambos
# imprima ‘PumBla’.

def sequencia(p, u):

    for c in range(p, u):
        if c % 3 != 0 and c % 5 != 0:
            print(c)

        elif c % 3 == 0 and c % 5 == 0:
            print('PumBla=>',c)

        elif c % 3 == 0:
            print('Bla====>',c)

        elif c % 5 == 0:
            print('Pum====>',c)

if __name__ == '__main__':
    print()
    print('Olá, indicamos para você dois números o 23(primeiro) e o 83(último), boa sorte!!!')
    print()
    p = int(input('Bem, qual é o primeiro número da sequência?===>: '))
    print()
    u = int(input('E, qual é o último número da sequência?===>: '))
    print()
    print('-' * 60)

    sequencia(p,u)

    print('-' * 60)
    print()
    print ("Obrigado por você ter participado desse exprimento.")


