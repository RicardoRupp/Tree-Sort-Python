# Programa em Python3 para
# implementar Tree Sort

# Classe contendo o filho da esquerda
# e da direita do nó atual
# e o valor da chave
class Node:

  def __init__(self, item=0):
    self.key = item
    self.left, self.right = None, None


# Raiz da árvore binária de busca (BST)
root = None


# Este método principalmente
# chama insertRec()
def insert(key):
  global root
  root = insertRec(root, key)


# Função recursiva para
# inserir uma nova chave na BST
def insertRec(root, key):

  # Se a árvore estiver vazia,
  # retorna um novo nó
  if (root == None):
    root = Node(key)
    return root

  # Caso contrário,
  # continua descendo na árvore
  if (key < root.key):
    root.left = insertRec(root.left, key)

  elif (key > root.key):
    root.right = insertRec(root.right, key)

  # retorna a raiz
  return root


# Função para realizar
# percurso em ordem (inorder) da BST
def inorderRec(root):

  if (root != None):

    inorderRec(root.left)

    print(root.key, end=" ")

    inorderRec(root.right)


# Insere todos os elementos do vetor
def treeins(arr):

  for i in range(len(arr)):
    insert(arr[i])


# Código principal

quantidade = int(input("Digite a quantidade de elementos: "))

arr = []

for i in range(quantidade):

  valor = int(input(f"Digite o {i+1}º valor: "))

  arr.append(valor)


treeins(arr)

print("\nVetor ordenado:")

inorderRec(root)
