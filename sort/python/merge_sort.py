# Divided happens in O(log n) time
# Compare each sub array takes O(n) time
# Overall for merge sort takes O(nlogn) time complexity
def mergeSort(arr, s, e):
  if (e - s + 1) <= 1:
    return arr

  mid = (s + e) // 2

  mergeSort(arr, s, mid)
  mergeSort(arr, mid + 1, e)

  merge(arr, s, mid, e)

  return arr

def merge(arr, s, mid, e):
  left = arr[s:mid + 1]
  right = arr[mid + 1:e + 1]
 
  # Pointer for sub array
  i = 0 # left array pointer
  j = 0 # right array pointer
  k = s # array sort pointer

  while i < len(left) and j < len(right):
    if right[j] < left[i]:
      arr[k] = right[j]
      j += 1
    else:
      arr[k] = left[i]
      i += 1
    k += 1

  # One of the halfs will have elements remaining
  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1
  
  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1

arr = [3,4,2,6,10,11]
print(mergeSort(arr, 0, len(arr) - 1))