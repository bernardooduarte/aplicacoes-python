# -*- coding: utf-8 -*-
"""Cópia de Operador condicional.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s4HfSgvdldIHQf1KOSQesHBogyGa8pkZ

# Operador condicional
"""

5 > 3

if 5 > 3:
    print('5 é maior que 3')
#print('teste')

if 5 > 4:
    print('5 é maior')
else:
    print('5 não é maior')

n = 9
if n == 4:
  print('n é igual a 4')
else:
  if n == 3:
    print('n é igual a 3')
  else:
    print('n não é igual a 4 nem 3')

x = 1
y = 5
if(x > 1) or (y % 2 == 0):
  print('x é maior que 1 e y é par')
else:
  print('Uma ou nenhuma das condições foram satisfeitas')