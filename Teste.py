# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool


'''nome = 'Tiago'
sobrenome = 'Lombardi'
idade = 9
ano_de_nascimento = 2023 - idade
maior_de_idade = idade >= 18
altura = 1.50

print('nome:', nome)
print('sobrenome:', sobrenome)
print('idade:', idade)
print('ano de nascimento:', ano_de_nascimento)
print('maior de idade?', maior_de_idade)
print('altura:', altura)'''


'''adicao = 10 + 20
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)'''


'''concatenacao = 'Pedroca' + ' ' + 'Miguel'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_pedro = 3 * 'Pedro '
print(a_dez_vezes)
print(tres_vezes_pedro)

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)'''


'''nome = 'Pedro'
idade = '19'
altura = 1.71
peso = 67
imc = peso / altura ** 2

linha_1 = f'{nome} tem {idade} anos de idade'
linha_2 = f'tem: {altura:.2f}, de altura'
linha_3 = f'pesa: {peso}, e seu imc é de: {imc:.2f}'

print(linha_1) 
print(linha_2) 
print(linha_3)'''


#nome = input('qual seu nome?')
#print(f'o seu nome é {nome=}')

'''numero_1 = input('digite um numero: ')
numero_2 = input('digite outro numero: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'a soma dos numeros é', {int_numero_1 + int_numero_2})'''


'''entrada = input('você deseja "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('voce entrou no sistema.')
elif entrada == 'sair':
    print('você saiu.')
else:
    print('erro, digite novamente')'''


'''maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')'''

'''
variavel_1 = input('Digite um valor: ')
variavel_2 = input('Digite outro valor: ')

if variavel_1 < variavel_2:
    print('o primeiro valor é menor que o segundo valor')
elif variavel_1 > variavel_2:
    print('o primeiro valor é maior que o segundo')
else:
    print('os valores são iguais')'''


#nome = input('digite seu nome: ')
#print(f'bem vindo {nome}')


"""nome = 'pedro'
preco = 5.500
variavel = '%s o preço é de %.3f' % (nome, preco)
print(variavel)"""


'''variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')'''


'''nome = input('qual seu nome? ')
idade = input('qual é a sua idade? ')
if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome de tás pra frente é: {nome [::-1]}')
    if ' ' in nome:
        print(f'seu nome contem espaços ')
    else: 
        print('seu nome não contém espaços')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}') 
    print(f'seu nome tem {len(nome)} letras')
else:
    print('voce deixou algum campo em branco... ')'''


'''velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')'''


'''condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')'''


nome = 'pedro lombardi' 
indice = 0
novo_nome = ''
nome2 = 'miguel'

while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1

print(novo_nome)
nomec = novo_nome[:6] + ' ' + nome2 [7:] + ''
print(nomec)
