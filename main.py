import os

n1 = int(input("Digite um número de 0 a 60: "))

os.system('clear')

if (n1 > 0 and n1 < 60):
  result = n1-1
  print("O sucessor de",n1,"é: ",result)
elif(n1 == 60):
  print("O sucessor de 60 é: 0")
else:
  print("número invalido")