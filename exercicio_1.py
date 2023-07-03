'''numero_digitado = input('Digite um valor: ')

if numero_digitado % 2 == 0:
    print(f'O número {numero_digitado} é par')
else: 
    print(f'O número {numero_digitado} é impar')'''

hora = input('Digite as horas: ')

if 12 <= hora <= 17:
    print('Boa tarde!')
elif 18 <= hora <= 23 or 0 <= hora <= 4:
    print('Boa noite!')
elif 5 <= hora <= 11:
    print('Bom dia!')
else:
    print('Hora inválida.')