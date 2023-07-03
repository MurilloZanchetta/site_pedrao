METAS_CONSUMO = 5000

ganhos = 0.0
while True:
    try:
        entrada = (input('digite seus ganhos, ou [n] para encerrar: '))
        if entrada.lower().startswith('n'):
            break
        ganhos = float(entrada)
    except:
        print('digite apenas numeros')

poupança = 0.0
while True:
    entrada_2 = input("você possui uma poupança? [s] ou [n]")
    if entrada_2.lower().startswith('s'):
        entrada_2 = input('digite o valor armazenado em sua poupança: ')
        break
    elif entrada_2.lower().startswith('n'):
        break
    poupança = float(entrada_2)

contas = 0.0
divida = 1

while True:
    try:
        entrada_divida = input(f'Digite sua {divida}ª dívida ou [n] para encerrar: ')
        if entrada_divida.lower() == 'n':
            break
        contas += float(entrada_divida)
        divida += 1
    except ValueError:
        print('Digite apenas números!')

print(f"Total das dívidas: R$ {contas}")

