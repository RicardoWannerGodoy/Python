# 9. Escreva uma função que faz um loop sobre as keys de um dicionário. Se as keys forem
# vogais, eleve o valor ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’.
print()
print('Olá, você irá nos ajudar a compor nosso dicionário digite a seguir um Vogais ou uma Consoantes.')
print()
print('Observaçao: Quando você quiser parar de incluir as letras é só digitar a palavra "fim".')
print()
print('-' * 95)

novodic = {}
while True:
    v = input('Por favor, digite uma Vogal ou Consoante para incluí-la ao dicionário.==>:')
    if v == 'fim':
        break
    novodic.update({v:len(novodic)+2})

print('-' * 95)
print()

print('Bem, segue abaixo o dicionário que você acabou de criar.')
print (novodic)

def finaldic (d):
  for vlletra in d:
    if vlletra in 'aeiouAEIOU':
      d[vlletra] = d[vlletra] ** 2
    else:
      d[vlletra] = 0
  print('-' * 65)
  print()

  print('Então, aqui temos o resultado do nosso exprimento,')
  print('"VOGAIS" elevada ao quadrado e "CONSOANTES" com o valor zerado:')
  print(d)

if __name__ == '__main__':
    d = novodic
    finaldic(d)
    print('-' * 65)
    print()
    print('Espero que você tenha gostado dessa brincadeira.')