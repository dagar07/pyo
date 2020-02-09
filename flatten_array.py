def flatten_array(arr = []):
  if not bool(arr):
    return 'Invalid Array from user'
  
  modifiedArr = []
  for item in arr:
    if isinstance(item, list):
      modifiedArr.extend(flatten_array(item))
    else:
      modifiedArr.append(item)
  return modifiedArr
  
print(flatten_array([[1, 2, 3], 4, [5, [6, 7, [8, 9, 10]]]]))
