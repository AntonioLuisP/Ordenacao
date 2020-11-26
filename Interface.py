from Ordenacao import Ordenacao
import PySimpleGUI as sg

class Interface:
  def __init__(self):
    self.erro = None

  def inicio(self):
    layout = [
      [sg.Text('Escolha o arquivo .txt onde está descrita a ordenação')],
      [sg.Text('Padrão do arquivo: primeira linha a quantidade de elementos e segunda um dos seguintes algoritmos:')],
      [sg.Text('Shell Sort, Heap Sort,Merge Sort ou Selection Sort')],
      [sg.FileBrowse(key='caminho')],
      [sg.Button('Continuar'),sg.Button('Sair')],
    ]
    janela = sg.Window("Programa pra ordenação de listas").layout(layout)
    button, values = janela.Read(close=True)
    if button == 'Continuar':
      if values['caminho']:
        info = self.infoArquivo(values['caminho'])
        tamanho = info['n']
        algoritmo = info['algoritmo']
        if algoritmo == 'shell sort'or algoritmo == 'heap sort' or algoritmo == 'merge sort' or algoritmo == 'selection sort':
          self.ordenador = Ordenacao(tamanho, algoritmo)
          janela.close()
          self.ordenar()
        else:
          self.inicio()
      else:
        self.inicio()
    if button == 'Sair':
      janela.close()
    if button == sg.WIN_CLOSED:
      janela.close()

  def ordenar(self):
    layout = [
      [sg.Text('Algoritmo escolhido: ' + self.ordenador.algoritmo.upper())],
      [sg.Button('Ordenar todos'), sg.Button('Ordenar Melhor Caso'), sg.Button('Ordenar Pior Caso'),sg.Button('Ordenar Medio Caso'),sg.Button('Voltar'),sg.Button('Sair')],
      [sg.Output(size=(80,30))],
    ]
    janela = sg.Window("Programa pra ordenação de listas").layout(layout)
    status = True
    while status:
      button, values = janela.Read()
      if button == 'Sair' or  button == sg.WIN_CLOSED:
        break
      if button == 'Ordenar todos':
        self.ordenador.testes()
      if button == 'Ordenar Melhor Caso':
        self.ordenador.testeMelhorCaso()
      if button == 'Ordenar Pior Caso':
        self.ordenador.testePiorCaso()
      if button == 'Ordenar Medio Caso':
        self.ordenador.testeMedioCaso()
      if button == 'Voltar':
        status = False
        janela.close()
        self.inicio()

                
  def infoArquivo(self, caminho):
    arquivo = open(caminho, 'r')
    info = {}
    algoritmo = []
    n = arquivo.readline().rstrip('\n')
    for i in arquivo:
      algoritmo  = i.rstrip('\n')
    info = {
      'n': int(n),
      'algoritmo': algoritmo.lower(),
    }
    arquivo.close()
    return info

tela = Interface()
tela.inicio()



