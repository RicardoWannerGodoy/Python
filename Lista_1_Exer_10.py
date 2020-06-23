#  10. Escreva uma função que retorna os máximos e mínimos de um dicionário.

dic={0: 3.498, 1: 1.098, 2: 12.898, 3: 21.398, 4: 1.298}

max_valor = max(dic.values())
print('*********')
min_valor = min(dic.values())
print('*Mínimo =>')
print(min_valor,'\n', max_valor)
print('<= Máximo*')
print('*********')