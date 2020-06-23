""" 1. Escreva um programa que imprima o seguinte padrão.
*
* *
* * *
* * * *
* * *
* *
*
"""

tamanho_maximo = 1
espacamento = 1

for i in range(1, tamanho_maximo + 1):
    # 1
    print("*" * i, end=" " * (tamanho_maximo - i + espacamento))
    print()

for i in range(1, tamanho_maximo + 1):
    # 2
    print("* *" * i, end = " " * (tamanho_maximo - i + espacamento))
    print()

for i in range(1, tamanho_maximo + 1):
    # 3
    print("* * *" * i, end = " " * (tamanho_maximo - i + espacamento))
    print()

for i in range(1, tamanho_maximo + 1):
    # 4
    print("* * * *" * i, end=" " * (tamanho_maximo - i + espacamento))
    print()

for i in range(1, tamanho_maximo + 1):
    # 3
    print("* * *" * i, end = " " * (tamanho_maximo - i + espacamento))
    print()

for i in range(1, tamanho_maximo + 1):
    # 2
    print("* *" * i, end=" " * (tamanho_maximo - i + espacamento))
    print()

for i in range(1, tamanho_maximo + 1):
    # 1
    print("*" * i, end=" " * (tamanho_maximo - i + espacamento))
    print()

