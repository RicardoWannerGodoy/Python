# 14. Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
# vez do parágrafo fornecido pelo usuário.

def counter(text):

    count_list = []

    for char in "abcdefghijklmnopqrstuvwxyz":
        count_list.append(text.lower().count(char))
    return tuple(count_list)

print('Olá! Qual é o seu nome?')
myName = input()
print()
print('Bem, '+ myName +', vamos continuar a nossa brincadeira.')
print()
x = input("Digite uma frase que iremos contar as letras repetidas: ")
print()

print('-' * 80)
print(counter(x))
print("(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)")
print('-' * 80)
print()
print('Bem, '+ myName +', confira a quantidade de letras que apareceram na frase digitada por você.')

