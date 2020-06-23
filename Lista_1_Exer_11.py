# 11. Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
# de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}.

listanova = [ ]
print()
print ('Olá, iremos construir uma "LISTA de 0 a 5" mas para isso preciso da sua ajuda.')
print()
print('-' * 60)
listanova.append(int(input('Digite o 1º número da sua "LISTA de NÚMEROS."==>:' )))
listanova.append(int(input('Digite o 2º número da sua "LISTA de NÚMEROS."==>:' )))
listanova.append(int(input('Digite o 3° número da sua "LISTA de NÚMEROS."==>:' )))
listanova.append(int(input('Digite o 4º número da sua "LISTA de NÚMEROS."==>:' )))
listanova.append(int(input('Digite o 5º número da sua "LISTA de NÚMEROS."==>:' )))
listanova.append(int(input('Digite o 6º número da sua "LISTA de NÚMEROS."==>:' )))
listanova.append(int(input('Digite o 7º número da sua "LISTA de NÚMEROS."==>:' )))

print('-' * 60)
print()
print('Essa é a sua "LISTA de NÚMEROS.==>:',listanova)
print()
print('-' * 75)

print('Agora vamos ordena-la do menor para o maior número.')
print()

listaordenada = sorted(listanova, key=None, reverse=False)
print('Veja como ficou ordenada a sua "LISTA de NÚMEROS.==>:',listaordenada)
print()
print('-' * 90)

listaindic = dict()
for each in listaordenada:
  listaindic[each] = listaindic.get(each, 0) + 1
print ('Enfim, essa é a sua LISTA de NÚMEROS com os seus indices:===>',listaindic)
