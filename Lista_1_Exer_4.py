# 4. Escreva um programa que ache e imprima os números divisíveis por 13 e por 19, entre o ano
# de nascimento da sua mãe e 2727.

def idademae(num):

    print('Sequência dos números divisíveis por 13')
    for c in range(num, 2727, 13):
        print(c, end=' ')
    print('<= FIM da divisão por 13')

    for c in range(num, 2727, 19):
        print(c, end=' ')
    print('<= FIM da divisão por 19')
    print('Sequência dos números divisíveis por 19')
    print('-' * 75)

    print()
    print('Bem, veja agora os números que são divisíveis por 13 e 19 ao mesmo tempo:')
    for c in range(num, 2727):
        if c % 13 == 0 and c % 19 == 0:
            print(c, end=' ')
    print()

if __name__ == '__main__':
    print()
    n = int(input('Bem, qual é o ano de nascimento da sua mãe?: '))
    print('-' * 75)
    idademae(n)
    print('-' * 75)

print()
print ("Obrigado por você ter participado dessa brincadeira.")