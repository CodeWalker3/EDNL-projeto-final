from tkinter import *
from PIL import ImageTk, Image
import time


class PilhaDuplamenteEncadeada:

  class Node:

    def __init__(self, valor, proximo=None, anterior=None):
      self.valor = valor
      self.proximo = proximo
      self.anterior = anterior

  def __init__(self):
    self.topo = None
    self.inicio = None
    self.tamanho = 0

  def vazio(self):
    return self.tamanho == 0

  def printarstack(self):
    no = self.topo
    temp = []
    while no is not None:
      temp.append(no.valor)
      no = no.anterior
      return temp

    return temp

  def ver_topo(self):
    if self.vazio():
      return None
    return self.topo.valor

  def empilheirar(self, valor):
    new_node = self.Node(valor, proximo=self.topo)
    if self.vazio():
      self.inicio = new_node
    else:
      self.topo.anterior = new_node
    self.topo = new_node
    self.tamanho += 1

  def remover_inicio(self):
    if self.vazio():
      return None
    valor = self.topo.valor
    self.topo = self.topo.proximo
    if self.topo is not None:
      self.topo.anterior = None
    else:
      self.inicio = None
    self.tamanho -= 1
    return valor


class MazeSolver:

  def __init__(self, maze):
    self.maze = maze
    self.start = self.encontrar_inicio()
    self.end = self.encontrar_final()
    self.stack = PilhaDuplamenteEncadeada()
    self.stack.empilheirar((self.start, [self.start]))

  def encontrar_inicio(self):
    for row in range(len(self.maze)):
      for col in range(len(self.maze[0])):
        if self.maze[row][col] == 'M':
          return row, col
    return None

  def encontrar_final(self):
    for row in range(len(self.maze)):
      for col in range(len(self.maze[0])):
        if self.maze[row][col] == 'E':
          return row, col
    return None

  def posicao_valida(self, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
      return False
    if pos_r >= len(self.maze) or pos_c >= len(self.maze[0]):
      return False
    if self.maze[pos_r][pos_c] in '.1':
      return False
    return True

  def print_maze(self):
    for row in self.maze:
      for item in row:
        print(item, end='')
      print()

  def exit_maze(self):

    while True:
      pos, path = self.stack.remover_inicio()
      pos_r, pos_c = pos
      if pos == self.encontrar_final():
        print("Alcançou o objetivo")
        self.maze[pos_r][pos_c] = "X"
        self.print_maze()
        print(path)
        return path

      if self.posicao_valida(pos_r + 1, pos_c):
        self.stack.empilheirar(((pos_r + 1, pos_c), path + [(pos_r + 1, pos_c)]))
      if self.posicao_valida(pos_r, pos_c - 1):
        self.stack.empilheirar(((pos_r, pos_c - 1), path + [(pos_r, pos_c - 1)]))
      if self.posicao_valida(pos_r - 1, pos_c):
        self.stack.empilheirar(((pos_r - 1, pos_c), path + [(pos_r - 1, pos_c)]))
      if self.posicao_valida(pos_r, pos_c + 1):
        self.stack.empilheirar(((pos_r, pos_c + 1), path + [(pos_r, pos_c + 1)]))
      self.maze[pos_r][pos_c] = '.'


maze = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1'],
        ['M', '0', '1', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '1'],
        ['E', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

labirinto = MazeSolver(maze)
# labirinto.exit_maze()
posRatoY = labirinto.encontrar_inicio()[0]
posRatoX = labirinto.encontrar_inicio()[1]
print(posRatoX, " x")
print(posRatoY, " y")
posicaoRatoY = (labirinto.encontrar_inicio()[0]) * 40
posicaoRatoX = (labirinto.encontrar_inicio()[1]) * 40
posicaoQueijoY = (labirinto.encontrar_final()[0]) * 40
posicaoQueijoX = (labirinto.encontrar_final()[1]) * 40

labirinto1 = labirinto.exit_maze()
print(labirinto1)


class Rato():

  def __init__(self, cordX, cordY, imageRato, canvas):
    self.cordX = cordX
    self.cordY = cordY
    self.imageRato = imageRato
    self.canvas = canvas

    RatoEnv = self.canvas.create_image(self.cordX,
                                       self.cordY,
                                       image=self.imageRato,
                                       anchor=NW)

    self.image = RatoEnv


class App(object):

  def __init__(self, app, maze, **kwargs):
    self.maze = maze
    self.app = app
    self.canvas = Canvas(self.app, width=842, height=842)
    self.canvas.pack()

    global imageRato
    global imageQueijo

    imageRato = ImageTk.PhotoImage(Image.open('rato.png').resize((30, 30)))
    imageQueijo = ImageTk.PhotoImage(Image.open('queijo.png').resize((30, 30)))

    for row in range(len(self.maze)):
      for col in range(len(self.maze[0])):
        if self.maze[row][col] == "1":
          self.canvas.create_rectangle(col * 40,
                                       row * 40, (col + 1) * 40,
                                       (row + 1) * 40,
                                       fill="black")
        elif self.maze[row][col] == "M":
          self.canvas.create_rectangle(col * 40,
                                       row * 40, (col + 1) * 40,
                                       (row + 1) * 40,
                                       fill="blue")
        elif self.maze[row][col] == "E":
          self.canvas.create_rectangle(col * 40,
                                       row * 40, (col + 1) * 40,
                                       (row + 1) * 40,
                                       fill="green")
        else:
          pass

    rato = Rato(posicaoRatoX, posicaoRatoY, imageRato, self.canvas)
    queijo = self.canvas.create_image(posicaoQueijoX,
                                      posicaoQueijoY,
                                      image=imageQueijo,
                                      anchor=NW)
    posis = labirinto1[0]
    posicaoInicialX = posis[1]
    posicaoInicialY = posis[0]

    tamanho = len(labirinto1)

    for index in range(1, tamanho):
      posicao = labirinto1[index]
      posiy = posicao[0]
      posix = posicao[1]

      if posiy > posicaoInicialY and posix == posicaoInicialX:
        x = 0
        y = 40
        posicaoInicialX = posix
        posicaoInicialY = posiy

      if posiy < posicaoInicialY and posix == posicaoInicialX:
        x = 0
        y = -40
        posicaoInicialX = posix
        posicaoInicialY = posiy

      if posiy == posicaoInicialY and posix > posicaoInicialX:
        x = 40
        y = 0
        posicaoInicialX = posix
        posicaoInicialY = posiy

      if posiy == posicaoInicialY and posix < posicaoInicialX:
        x = -40
        y = 0
        posicaoInicialX = posix
        posicaoInicialY = posiy

      self.canvas.move(rato.image, x, y)
      root.update()
      time.sleep(0.5)


root = Tk()
root.title('MazeSolver')
app = App(root, maze)

root.mainloop()
