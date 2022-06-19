import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Claro! Você deve',
            'Sim, agora', 
            'Com certeza não',
            'Acho melhor não'
        ]
    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Decida por mim')]
        ]
        #janela 
        self.janela = sg.Window('Decida por Mim', layout=layout)
        while True: 
            #ler os valores
            self.eventos, self.valores = self.janela.Read()
            #fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
                
decida = DecidaPorMim()
decida.Iniciar()