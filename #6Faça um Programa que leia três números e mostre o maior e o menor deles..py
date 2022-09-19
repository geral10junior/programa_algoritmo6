#7Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = input('Informe o primeiro número: ')
n2 = input('Informe o segundo número: ')
n3 = input('Informe o terceiro número: ')

print('O maior e o menor número respectivamente são:')

if n1 < n2 < n3: 
    print (n1, n3)
elif n1 < n3 < n2:
    print (n1, n2)
elif n2 < n1 < n3:
    print (n2, n3)
elif n2 < n3 < n1:
    print (n2, n1)
elif n3 < n1 < n2:
    print (n3, n2)   
else:
    print(n3, n1)