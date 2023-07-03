class JogoAventura:
    def __init__(self):
        self.jogando = True

    def jogar(self):
        entrada = input("Jogar? 'sim' ou 'nao': ")
        
        if entrada == 'sim':
            print('Você escolheu entrar.')
        elif entrada == 'nao':
            print('Você escolheu não jogar.')
            self.jogando = False
        else:
            print('Você morreu.')
            self.jogando = False
            return

        while self.jogando:
            print('Você está perdido, o que fazer?') #escolhas - 1
            print('1- Buscar abrigo')
            print('2- Beber água do rio')
            print('3- Chorar')
            entrada_2 = input('Escolha uma opção: ')

            if entrada_2 == '1': #abrigo
                print('Você decidiu buscar abrigo.')
                print('Você anda por horas em uma floresta fria e escura.')
                print('Você anda por tanto tempo que começa a escurecer.')
                print('O clima fica gelado e consequentemente mais perigoso.')
                print('Você encontra uma cabana vazia, mas que já foi habitada.')
                print('O que fará agora?')
                print('1- Dormir')
                print('2- Preparar um chá (ficar acordado)')
                entrada_a = input('Escolha uma opção: ')
                if entrada_a == '1':
                    print('Você decidiu dormir.')
                    print('Você tem pesadelos durante a noite.')
                    print('"Como vim parar aqui? Como farei para sair?"')
                    print('Vozes ecoam na sua cabeça.')
                    print('Você acorda totalmente revigorado.')
                    print('A floresta não parece um lugar ruim agora.')
                    print('O que você vai fazer agora?')
                    print('1- Caminhar na floresta')
                    print('2- Beber água do rio')
                    print('3- Chorar')
                elif entrada_a == '2':
                    print('Você decidiu fazer um chá, às 00:59am.')
                    print('Você acredita fortemente que beber um chá resolverá seus problemas.')
                    print('O seu chá é horrível.')
                    print('Você se contorce de desgosto.')
                    print('Você morreu.')
                    morte_1 = input('Deseja continuar? ')
                    if morte_1 == 'sim':
                        continue
                    elif morte_1 == 'nao':
                        self.jogando = False
                else:
                    print('Opção inválida.')
                    self.jogando = False
            elif entrada_2 == '2': #desejo
                print('Você decidiu beber água do rio.')
                print('Chegando no rio você se depara com algo brilhante no chão.')
                print('É uma lâmpada 🤩')
                print('Você tem direito a 1 pedido apenas.')
                print('1- Físico mais estético')
                print('2- Ficar extremamente rico')
                print('3- Uma arma de combate')
                entrada_f = input('Escolha uma opção: ')
                if entrada_f == '1': #opção físico
                    print('Você escolheu ter um físico mais estético.')
                    print('Zyzz está orgulhoso de você, filho...')
                    print('Você sente agora que está pronto para continuar sua jornada.')
                    print('O que você vai fazer agora?')
                elif entrada_f == '2':
                    print('Você escolheu ficar extremamente rico...')
                    print('Ao seu lado, surge uma quantidade enorme de barras de ouro.')
                    print('Porém, você sente um pressentimento estranho...')
                    escolha_principal_1 = input('O que você vai fazer agora?')
                    print('1- Buscar abrigo')
                    print('3- Chorar')
                elif entrada_f == '3':
                    print('Você escolheu ter uma arma de combate.')
                    print('Uma espada mágica surge em suas mãos.')
                    print('Agora você está pronto para enfrentar qualquer desafio.')
                    print('')
                elif entrada_f == '1' == input('chupa meu cu'):
                    print('sim') 
                
                else:
                    print('Opção inválida.')
                    self.jogando = False
            elif entrada_2 == '3': #chorar
                print('Você decidiu que chorar seria a solução de seus problemas...')
                print('Você fez tanto barulho chorando que atraiu um urso-pardo.')
                print('Ele se aproxima, o que você vai fazer?')
                print('1- Matar o urso')
                print('2- Domesticar o urso')
                print('3- Correr')
                entrada_c = input('Escolha uma opção: ')
                if entrada_c == '1': #morre
                    print('Você decidiu matar o urso.')
                    print('Você tenta matar o urso.')
                    print('O urso esmaga seu crânio.')
                    print('Você morreu.')
                    morte_1 = input('Deseja continuar? ')
                    if morte_1 == 'sim':
                        continue
                    elif morte_1 == 'nao':
                        self.jogando = False
                elif entrada_c == '2': #morre
                    print('Você escolheu domar o urso.')
                    print('Você tenta domar um urso selvagem...')
                    print('Patético.')
                    print('Ele fica confuso e te ataca.')
                    print('Você morreu.')
                    self.jogando = False
                elif entrada_c == '3': #morre
                    print('Você escolheu correr.')
                    print('Você tenta correr do urso selvagem.')
                    print('Ele te alcança e te mata.')
                    print('Você morreu.')
                    morte_1 = input('Deseja continuar? ')
                    if morte_1 == 'sim':
                        continue
                    elif morte_1 == 'nao':
                        self.jogando = False
                else:
                    print('Opção inválida.')
                    self.jogando = False
            else:
                print('Opção inválida.')
                self.jogando = False

        print('Fim do jogo.')


def main():
    jogo = JogoAventura()
    while True:
        jogo.jogar()
        reiniciar = input('Deseja reiniciar o jogo? (sim/nao): ')
        if reiniciar.lower() != 'sim':
            break


if __name__ == '__main__':
    main()