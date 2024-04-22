def quickSort(arr, s, e):
  if (e - s + 1) <= 1:
    return

  pivot = arr[e]
  left = s

  for i in range(s, e):
    if arr[i] < pivot:
      tmp = arr[i]
      arr[i] = arr[left]
      arr[left] = tmp
      left += 1
  
  arr[e] = arr[left]
  arr[left] = pivot

  quickSort(arr, s, left - 1)
  quickSort(arr, left + 1, e)
  return arr

arr = [3,4,2,6,10,11]
print(quickSort(arr, 0, len(arr) - 1))