class Pilha:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop(0)

  def is_empty(self):
    return len(self.items) == 0

  def size(self):
    return len(self.items)

  def remove_last(self):
    if len(self.items) > 0:
      self.items.pop()

pilha = Pilha()

while pilha.size() < 10:
  arg = int(input('Insira um item na pilha:'))
  print('Insira 000 para parar')
  if arg == 000:
    break
  pilha.push(arg)
  print(pilha.items)

print(pilha.items)

opc = input('para remover o último item digite - ')
if opc == '-':
    item = pilha.remove_last()

print(pilha.items)
