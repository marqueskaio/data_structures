class Fila:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)

  def is_empty(self):
    return len(self.items) == 0

  def size(self):
    return len(self.items)

fila = Fila()

while fila.size() < 10:
  arg = int(input('Insira um item na fila:'))
  print('Insira 000 para parar')
  if arg == 000:
    break
  fila.enqueue(arg)
  print(fila.items)

print(fila.items)

opcao = input('para remover o primeiro item digite - ')
if opcao == '-':
    item = fila.dequeue()

print(fila.items)

