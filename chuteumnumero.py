# objetivo -> Criar um algoritmo que gere um número no backend,
# enquanto a pessoa tem que acerta-lo tentando vários numeros
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('seu chute', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(40,10))]
        ]
        #criar janelam 
        self.janela = sg.Window('Chute o número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #receber valores
                self.LerValoresDaTela()
                #fazer algo valores
                if self.evento == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais Baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabéns! Você acertou!')
                            break
        except:
            print('Favor digitar APENAS números')
            self.Iniciar()


    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read() 


    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
        
chute = ChuteONumero()
chute.Iniciar() 
