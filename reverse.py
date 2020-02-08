def reverse(list):
  if not bool(list):
    return 'Empty List'
  
  if len(list) == 1:
    return list
  index = 0
  lastIndex = len(list) - 1
  for val in range(len(list)):
    if index < lastIndex:
      temp = list[index]
      list[index] = list[lastIndex]
      list[lastIndex] = temp
      index = index + 1
      lastIndex = lastIndex - 1
    elif lastIndex < index:
      break
  print(list)

reverse([1])