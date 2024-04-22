# O(n) time complexity
# Stable sorting algorithm
def insertionSort(arr):
  # Traverse the array
  for i in range(1, len(arr)):
    j = i - 1
    # Swap if arr[i] < arr[j]
    while j >= 0 and arr[j + 1] < arr[j]:
      tmp = arr[j + 1]
      arr[j + 1] = arr[j]
      arr[j] = tmp
      j -= 1
  return arr

print(insertionSort([3,4,2,6,10,11]))