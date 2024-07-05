class ListNode:
  def __init__(self, val) -> None:
    self.val = val
    self.next = None

class SinglyLinkedList:
  def __init__(self) -> None:
    self.head = ListNode(-1)
    self.tail = self.head

  # O(n) time complexity
  def accessElement(self, index):
    i = 0
    curr = self.head
    while i < index and curr:
      curr = curr.next
      i += 1
    if curr:
      return curr

  # O(1) time complexity
  def insertEnd(self, val):
    new_node = ListNode(val)
    self.tail.next = new_node
    self.tail = self.tail.next

  # O(n) time complexity
  def removeEnd(self):
    curr = self.head
    while curr.next is not self.tail:
      curr = curr.next
    curr.next = None
    self.tail = curr

  # O(1) time because doesn't need to shift rest of elements, 
  # but the caveat is to access i'th element in linked list takes O(n)
  # Most cases takes O(n) time complexity
  def insertMid(self, index, val):
    curr = self.accessElement(index)
    new_node = ListNode(val)
    new_node.next = curr.next
    curr.next = new_node
    return new_node.val

  # O(1) time because doesn't need to shift rest of elements, 
  # but the caveat is to access i'th element in linked list takes O(n)
  # Most cases takes O(n) time complexity
  def removeMid(self, index):
    curr = self.accessElement(index - 1)
    val = curr.next.val
    curr.next = curr.next.next
    return val

  def printNode(self):
    curr = self.head.next
    while curr:
      print(curr.val, "->")
      curr = curr.next  

singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insertEnd(1)
singlyLinkedList.insertEnd(2)
singlyLinkedList.insertEnd(3)
# singlyLinkedList.removeEnd()
# singlyLinkedList.insertMid(1,10)
print(singlyLinkedList.removeMid(1))
singlyLinkedList.printNode()

    