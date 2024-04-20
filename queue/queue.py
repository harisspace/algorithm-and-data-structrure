class Node:
  def __init__(self, data):
    self.val = data
    self.next = None

class Queue:
  def __init__(self):
    self.left = self.right = None

  # O(1) time complexity
  def enqueue(self, data):
    new_node = Node(data)

    if self.left:
      self.right.next = new_node
      self.right = new_node
    else:
      self.left = self.right = new_node

  def dequeue(self):
    if not self.left:
      raise ValueError("Empty queue")

    data = self.left.val
    self.left = self.left.next
    return data

  def printQueue(self):
    curr = self.left
    while curr:
      print(curr.val, "->")
      curr = curr.next

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.printQueue()
