# 7. Escreva um programa que, dada uma lista de números [-2, 34, 5, 10, 5, 4, 32] qualquer,
# retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
# *** Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
# (sorted()). Para listas pares, retorne os dois valores do meio.

import statistics

numlista = [ ]

print()
print ('Olá, iremos construir uma "LISTA de NÚMEROS" mas para isso preciso da sua ajuda.')
print()
print('-' * 80)
numlista.append(int(input('Então, digite o 1º número da sua nova "LISTA de NÚMEROS."==>:' )))
numlista.append(int(input('Então, digite o 2º número da sua nova "LISTA de NÚMEROS."==>:' )))
numlista.append(int(input('Então, digite o 3° número da sua nova "LISTA de NÚMEROS."==>:' )))
numlista.append(int(input('Então, digite o 4º número da sua nova "LISTA de NÚMEROS."==>:' )))
numlista.append(int(input('Então, digite o 5º número da sua nova "LISTA de NÚMEROS."==>:' )))
print('-' * 65)
print('Essa é a sua "LISTA de NÚMEROS.==>:',numlista)
print('-' * 75)

print('Agora vamos ordena-la do menor para o maior número.')
print()

listaord = sorted(numlista, key=None, reverse=False)
print('Veja como ficou ordenada a sua "LISTA de NÚMEROS.==>:',listaord)
print('-' * 75)

print('Esse é o menor valor da "LISTA de NÚMEROS.==>:',min(listaord))
print()

print('Esse é o maior valor da "LISTA de NÚMEROS.==>:',max(listaord))
print()

print('Essa é a soma dos valores da "LISTA de NÚMEROS.==>:',sum(listaord))
print()

print('Esse é a quantidade de itens da "LISTA de NÚMEROS.==>:',len(listaord))
print()

print('Esse é a média dos valores da "LISTA de NÚMEROS.==>:',statistics.mean(listaord))
print()

print('Esse é a mediana dos valores da "LISTA de NÚMEROS.==>:',statistics.median(listaord))
print('-' * 65)
print()

print('Bem, finalizamos, espero que você tenha gostado do exprimento.')
