class DynamicArray:
  def __init__(self, capacity) -> None:
    self.capacity = capacity 
    self.size = 0
    self.arr = [0] * capacity

  # O(1) time complexity
  def getSize(self):
    return self.size

  def getValue(self, index):
    if index < 0 or index > self.size:
      raise ValueError("Out of bound")
    return self.arr[index]

  # O(n) time complexity
  def resize(self):
    self.capacity *= 2
    newArr = [0] * self.capacity
    for i in range(self.size):
      newArr[i] = self.arr[i]
    self.arr = newArr
    return self.arr

  # O(1) time in average
  def append(self, val):
    if self.size >= self.capacity:
      self.resize()
    self.arr[self.size] = val
    self.size += 1
    return self.arr

  # O(1) time complexity
  def removeEnd(self):
    if self.size < 1:
      raise ValueError("Empty array")
    self.arr[self.size - 1] = 0
    self.size -= 1
    return self.arr

  # O(n) time complexity
  def printArr(self):
    arr = ''
    for i in range(self.size):
      arr += str(self.arr[i]) + "|"
    print(arr)

class Stack:
  def __init__(self, dynamicArray) -> None:
    self.arr = dynamicArray

  # O(1) time
  def push(self, val):
    self.arr.append(val)
    return self.arr
  
  # O(1) time
  def pop(self):
    self.arr.removeEnd()
    return self.arr

  # O(n) time complexity
  def printStack(self):
    arr = ''
    for i in range(self.arr.getSize()):
      arr += str(self.arr.getValue(i)) + "|"
    print(arr)

dynamicArr = DynamicArray(2)
stack = Stack(dynamicArr)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.printStack()