import random

simbolos = ["7", "Bar", "Cereja", "Uva"]
probabilidades = [0.23, 0.18, 0.55, 0.18]  # Probabilidades correspondentes a cada símbolo

def girar_rolos():
    rolos = []
    for _ in range(3):
        simbolo = random.choices(simbolos, probabilidades)[0]
        rolos.append(simbolo)
    return rolos

def verificar_combinacoes(rolos):
    if rolos[0] == rolos[1] == rolos[2]:
        return True
    return False

def jogo_caca_niquel():
    saldo = 100
    retencao = 0.1  # 10% de retenção

    while saldo > 0:
        print("Saldo atual:", saldo)
        aposta = int(input("Faça sua aposta: "))

        if aposta > saldo:
            print("Aposta maior que o saldo disponível. Tente novamente.")
            continue

        # Calcular a retenção
        valor_retencao = int(aposta * retencao)
        saldo -= valor_retencao

        # Girar os rolos
        rolos = girar_rolos()
        print("Resultado:", rolos)

        if verificar_combinacoes(rolos):
            premio = aposta * 2
            saldo += premio
            print("Parabéns! Você ganhou. Prêmio:", premio)
        else:
            saldo -= aposta  # Deduzir a aposta do saldo
            print("Você perdeu.")

    print("Saldo zerado. Fim de jogo.")

jogo_caca_niquel()
