from pympler import asizeof
import numpy as np
import time, tracemalloc
import csv, datetime

class Ordenacao:

  def __init__(self, n, algoritmo):
    self.gerarVetores(n, algoritmo)

  def gerarVetores(self, n, algoritmo):
    self.tamanho = n
    self.algoritmo = algoritmo
    self.melhorCaso = {
      'situacao': 'melhor',
      'vetor': list(range(n))
    }
    self.piorCaso = {
      'situacao': 'pior',
      'vetor': list(range(n,0,-1))
    }
    self.medioCaso1 = {
      'situacao': 'medio1',
      'vetor': list(np.random.randint(n, size=(n)))
    }
    self.medioCaso2 = {
      'situacao': 'medio2',
      'vetor': list(np.random.randint(n, size=(n)))
    }
    self.medioCaso3 = {
      'situacao': 'medio3',
      'vetor': list(np.random.randint(n, size=(n)))
    }
    self.medioCaso4 = {
      'situacao': 'medio4',
      'vetor': list(np.random.randint(n, size=(n)))
    }
    self.medioCaso5 = {
      'situacao': 'medio5',
      'vetor': list(np.random.randint(n, size=(n)))
    }
    self.medios = (
      self.medioCaso1,
      self.medioCaso2,
      self.medioCaso3,
      self.medioCaso4,
      self.medioCaso5
    )

  def testes(self):
    self.testeMelhorCaso()
    self.testePiorCaso()
    self.testeMedioCaso()

  def testeMelhorCaso(self):
    print('algoritmo: ', self.algoritmo,' Situação: ', self.melhorCaso['situacao'], " para: ", self.tamanho, " elementos")
    if self.algoritmo == "merge sort":
      info = self.complexidadeMerge(self.melhorCaso)   
    elif self.algoritmo == "selection sort":
      info = self.complexidadeSelection(self.melhorCaso)
    elif self.algoritmo == "shell sort":
      info = self.complexidadeShellSort(self.melhorCaso)
    elif self.algoritmo == "heap sort":
      info = self.complexidadeHeapSort(self.melhorCaso)
    algoritmo = self.algoritmo
    tamanho = self.tamanho
    situacao = self.melhorCaso['situacao']  
    tempo = info['tempo']
    memoria = info['memoria']
    self.escreveCsv(algoritmo,tamanho,situacao,tempo,memoria)
    print('Duracao da ordenacao ', tempo)
    print('Consumo de memória', memoria,'MB')
    print('-------------------------------------------------')

  def testePiorCaso(self):  
    print('algoritmo: ', self.algoritmo,' Situação: ', self.piorCaso['situacao'], " para: ", self.tamanho, " elementos")
    if self.algoritmo == "merge sort":
      info = self.complexidadeMerge(self.piorCaso)   
    elif self.algoritmo == "selection sort":
      info = self.complexidadeSelection(self.piorCaso)
    elif self.algoritmo == "shell sort":
      info = self.complexidadeShellSort(self.piorCaso)
    elif self.algoritmo == "heap sort":
      info = self.complexidadeHeapSort(self.piorCaso)
    algoritmo = self.algoritmo
    tamanho = self.tamanho
    situacao = self.piorCaso['situacao']
    tempo = info['tempo']
    memoria = info['memoria']
    self.escreveCsv(algoritmo,tamanho,situacao,tempo,memoria)
    print('Duracao da ordenacao ', tempo)
    print('Consumo de memória', memoria,'MB')
    print('-------------------------------------------------')

  def testeMedioCaso(self):
    media_tempo = 0
    media_memoria = 0
    soma_tempo = 0
    soma_memoria = 0
    qtd_medios = len(self.medios)
    print('algoritmo: ', self.algoritmo,' Situação: média para ', qtd_medios, ' vetores com ', self.tamanho, " elementos")
    for caso in self.medios:
      if self.algoritmo == "merge sort":
        info = self.complexidadeMerge(caso)   
      elif self.algoritmo == "selection sort":
        info = self.complexidadeSelection(caso)
      elif self.algoritmo == "shell sort":
        info = self.complexidadeShellSort(caso)        
      elif self.algoritmo == "heap sort":
        info = self.complexidadeHeapSort(caso)        
      tempo = info['tempo']
      memoria = info['memoria']
      soma_tempo += tempo
      soma_memoria += memoria
    algoritmo = self.algoritmo
    tamanho = self.tamanho
    situacao = 'medio'
    media_tempo = soma_tempo/qtd_medios
    media_memoria = soma_memoria/qtd_medios
    self.escreveCsv(algoritmo,tamanho,situacao,media_tempo,media_memoria)
    print('Duracao media da ordenacao ', media_tempo)
    print('Consumo medio de memória', media_memoria,'MB')
    print('-------------------------------------------------')

  def complexidadeMerge(self, caso):
    agora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print('comecou em:', agora)
    tracemalloc.start()
    inicio_ordenacao = time.time()
    self.mergeSort(caso['vetor'])
    fim_ordenacao = time.time()
    current, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    duracao_ordenacao = fim_ordenacao - inicio_ordenacao
    info = {
      'tempo': duracao_ordenacao,
      'memoria': current/10**6,
    }
    return info

  def complexidadeSelection(self, caso):
    agora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print('comecou em:', agora)
    tracemalloc.start()
    inicio_ordenacao = time.time()
    self.selectionSort(caso['vetor'])
    fim_ordenacao = time.time()
    current, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    duracao_ordenacao = fim_ordenacao - inicio_ordenacao
    info = {
      'tempo': duracao_ordenacao,
      'memoria': current/10**6,
    }
    return info
  
  def complexidadeShellSort(self, caso):
    agora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print('comecou em:', agora)
    tracemalloc.start()
    inicio_ordenacao = time.time()
    self.shellSort(caso['vetor'])
    fim_ordenacao = time.time()
    current, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    duracao_ordenacao = fim_ordenacao - inicio_ordenacao
    info = {
      'tempo': duracao_ordenacao,
      'memoria': current/10**6,
    }
    return info

  def complexidadeHeapSort(self, caso):
    agora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print('comecou em:', agora)
    tracemalloc.start()
    inicio_ordenacao = time.time()
    self.heapSort(caso['vetor'])
    fim_ordenacao = time.time()
    current, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    duracao_ordenacao = fim_ordenacao - inicio_ordenacao
    info = {
      'tempo': duracao_ordenacao,
      'memoria': current/10**6,
    }
    return info
  
  def mergeSort(self, vetor, inicio=0, fim=None):
    if fim is None:
      fim = len(vetor)
    if(fim - inicio > 1):
      meio = (fim + inicio)//2
      self.mergeSort(vetor, inicio, meio)
      self.mergeSort(vetor, meio, fim)
      self.merge(vetor, inicio, meio, fim)
    return vetor

  def merge(self, vetor, inicio, meio, fim):
    left = vetor[inicio:meio]
    right = vetor[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
      if top_left >= len(left):
        vetor[k] = right[top_right]
        top_right = top_right + 1
      elif top_right >= len(right):
        vetor[k] = left[top_left]
        top_left = top_left + 1
      elif left[top_left] < right[top_right]:
        vetor[k] = left[top_left]
        top_left = top_left + 1
      else:
        vetor[k] = right[top_right]
        top_right = top_right + 1

  def selectionSort(self, vetor):
    n = len(vetor)
    for index in range(0, n):
      min_index = index
      for right in range(index + 1, n):
        if vetor[right] < vetor[min_index]:
          min_index = right
      vetor[index], vetor[min_index] = vetor[min_index], vetor[index]
    return vetor

  def shellSort(self, vetor):
    sublistcount = len(vetor)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        self.gapInsertionSort(vetor,startposition,sublistcount)
      sublistcount = sublistcount // 2

  def gapInsertionSort(self, vetor,start,gap):
    for i in range(start+gap,len(vetor),gap):
      currentvalue = vetor[i]
      position = i
      while position>=gap and vetor[position-gap]>currentvalue:
        vetor[position]=vetor[position-gap]
        position = position-gap
      vetor[position]=currentvalue

  def heapify(self, vetor, n, i): 
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and vetor[i] < vetor[l]: 
      largest = l 
    if r < n and vetor[largest] < vetor[r]: 
      largest = r 
    if largest != i: 
      vetor[i],vetor[largest] = vetor[largest],vetor[i]
      self.heapify(vetor, n, largest) 
    
  def heapSort(self, vetor): 
    n = len(vetor)  
    for i in range(n//2 - 1, -1, -1): 
      self.heapify(vetor, n, i)     
    for i in range(n-1, 0, -1): 
      vetor[i], vetor[0] = vetor[0], vetor[i]
      self.heapify(vetor, i, 0) 

  def escreveCsv(self, algoritmo,tamanho,situacao,tempo,memoria):
    nome = 'desempenho ' + algoritmo + '.csv'
    with open(nome, 'a', newline='') as file:
      agora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
      writer = csv.writer(file)
      writer.writerow((agora,algoritmo,tamanho,situacao,tempo,memoria))
      