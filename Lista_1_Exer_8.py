# 8. Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que
# 8.1 acrescente um par (chave, valor) {‘b’: 1}, ao dicionário;
# 8.2 verifique se a key ‘c’ está presente?
# 8.3 Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método
# ‘update’!

print()
print('Olá, você irá nos ajudar a compor nossos dicionário digite as letras quando solicitado.')
print('OBSERVAÇÃO: Quando você quiser parar de incluir as letras é só digitar a palavra "fim".')
print()
print('-' * 95)
novodic1 = {}
item = 0
while True:
    v1 = input('Por favor, digite uma Vogal ou Consoante para incluí-la ao 1º dicionário: ==>  ')
    if v1 == 'fim':
        break
    novodic1.update({v1:len(novodic1)+item})
print('-' * 95)
print()
print('Bem, segue abaixo o 1ª dicionário que você acabou de criar.')
print (novodic1)
print('-' * 95)


print('OBSERVAÇÃO: Quando você quiser parar de incluir as letras é só digitar a palavra "fim".')
print()
print('-' * 95)
novodic2 = {}
item = 0
while True:
    v2 = input('Por favor, digite uma Vogal ou Consoante para incluí-la ao 2º dicionário: ==>  ')
    if v2 == 'fim':
        break
    novodic2.update({v2:len(novodic2)+item})
print('-' * 5)
print()
print('Ok, segue abaixo o 2ª dicionário que você acabou de criar.')
print (novodic2)
print('-' * 95)

print()
print('Então, nesse momento fizemos uma concatenação dos dois dicionários criados anteriormente.')
juncaodic12 = {}
juncaodic12.update(novodic1)
juncaodic12.update(novodic2)

print(juncaodic12)
print('-' * 95)

print()
print('Enfim, digite uma letra que iremos localiza-la no dicionário concatenado.')

busca = input('Qual a letra que você gostaria de saber se consta no dicionário concatenado:===>>  '  )
print('-' * 45)
print('Essa é a resposta da busca:===>>', busca in juncaodic12)
print('-' * 45)

print('OBSERVAÇÃO: Verifique a palavra que representa se achamos ou não a letra digitada:')
print('LEGENDA:        ===>> ( False ) = Não Consta    e    ===>> ( True ) = Consta.')

print('-' * 95)
print()
print('Finalizamos, espero que você tenha gostado dessa brincadeira.')














