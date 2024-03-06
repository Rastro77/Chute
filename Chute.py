'''
Escreva um programa que, ao iniciar gera um valor aleatório de 0 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.
O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no início do programa.

input chute
if chute > valor_aleatorio
  print "Chute foi maior que o valor gerado"
if chute < valor_aleatorio
  print "Chute foi menor que o valor gerado"
if chute = valor_aleatorio
  print "Você acertou!"
'''
#Chute um número aleatório de 0 a 10

import random

valor_aleatorio = random.randint(0,10)
acertou = False
while acertou == False:
  chute = int(input('Chute um valor de 0 a 10: '))
  if chute > valor_aleatorio:
    print('Chute foi maior que o valor gerado')
  elif chute < valor_aleatorio:
    print('Chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou!')
    
