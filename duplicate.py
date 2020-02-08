def duplicate(list):
  if not bool(list):
    return 'List empty'
  
  itemSet = set()
  for item in list:
    if item in itemSet:
      return True
    else:
      itemSet.add(item)
  
  return False

print(duplicate([1, 2, 3]))