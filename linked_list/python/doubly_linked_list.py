class ListNode:
  def __init__(self, val) -> None:
    self.val = val
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self) -> None:
    self.head = ListNode(-1)
    self.tail = self.head

  # O(n) time complexity
  def accessElement(self, index):
    curr = self.head
    i = 0
    while i < index and curr:
      curr = curr.next
      i += 1
    if curr:
      return curr
  
  # O(1) time complexity
  def insertEnd(self, val):
    new_node = ListNode(val)
    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

  # O(1) time complexity
  def removeEnd(self):
    self.tail = self.tail.prev
    self.tail.next = None

  # O(1) time because doesn't need to shift rest of elements, 
  # but the caveat is to access i'th element in linked list takes O(n)
  # Most cases takes O(n) time complexity
  def insertMid(self, val, index):
    new_node = ListNode(val)
    curr = self.accessElement(index)
    new_node.prev = curr
    new_node.next = curr.next
    curr.next = new_node
    new_node.next.prev = new_node

  # O(1) time because doesn't need to shift rest of elements, 
  # but the caveat is to access i'th element in linked list takes O(n)
  # Most cases takes O(n) time complexity
  def removeMid(self, index):
    curr = self.accessElement(index - 1)
    curr.next = curr.next.next
    curr.next.prev = curr

  def printList(self):
    curr = self.head
    while curr:
      print(curr.val, "->")
      curr = curr.next

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insertFront(1) 
doublyLinkedList.insertFront(2) 
doublyLinkedList.insertFront(3) 
doublyLinkedList.insertFront(5)
doublyLinkedList.insertMid(10,2)
doublyLinkedList.printList() 