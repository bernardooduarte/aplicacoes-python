# -*- coding: utf-8 -*-
"""EXERCÍCIOS 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15AJkpSZNS6ReNDTjT_ShB-cI1tlDnohl

# Exercício 1
"""

a = int(input())
b = int(input())

print(a, b)

adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print('Adição', adicao)
print('Subtração', subtracao)
print('Multiplicação', multiplicacao)
print('Divisão', round(divisao, 2))

"""# Exercício 2"""

tempo = float(input('Insira o tempo gasto na viagem: '))
velocidade = float(input('Insira a velocídade média durante a viagem: '))

print(tempo, velocidade)

distancia = tempo * velocidade
litros_usados = distancia / 12

print('Velocidade média:', velocidade)
print('Tempo gasto na viagem:', tempo)
print('Distãncia percorrida:', distancia)
print('Quantidade de litros utilizada na viagem:', round(litros_usados,1))