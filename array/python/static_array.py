class StaticArray:
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.size = 0
    self.arr = [0] * capacity

  # O(1) time complexity
  def append(self, val):
    if self.size >= self.capacity:
      raise ValueError("Max capacity")
    self.arr[self.size] = val
    self.size += 1
    return self.arr

  # O(n) time complexity
  def addFirst(self, val):
    if self.size >= self.capacity:
      raise ValueError("Max capacity")

    for i in range(self.size - 1, -1, -1):
      self.arr[i + 1] = self.arr[i]
    
    self.arr[0] = val
    self.size += 1
    return self.arr

  # O(n) time complexity
  def insertMiddle(self, val, index):
    if self.size >= self.capacity:
      raise ValueError("Max capacity")

    for i in range(self.size - 1, index - 1, -1):
      self.arr[i + 1] = self.arr[i]
    self.arr[index] = val
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
  def removeFirst(self):
    if self.size < 1:
      raise ValueError("Empty array")
    for i in range(1, self.size):
      self.arr[i - 1] = self.arr[i]
    self.size -= 1
    return self.arr

  # O(n) time complexity
  def removeMiddle(self, index):
    if self.size < 1:
      raise ValueError("Empty array")
    for i in range(index + 1, self.size):
      self.arr[i - 1] = self.arr[i]
    self.size -= 1
    return self.arr

  # O(n) time complexity
  def printArr(self):
    arr = ''
    for i in range(self.size):
      arr += str(self.arr[i]) + "|"
    print(arr)

staticArr = StaticArray(5)
staticArr.append(10)
staticArr.append(1)
staticArr.addFirst(20)
staticArr.insertMiddle(32, 1)
staticArr.removeEnd()
staticArr.removeFirst()
staticArr.removeMiddle(1)
staticArr.printArr()




