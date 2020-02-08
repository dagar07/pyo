def min_max(list):
  if len(list) < 2:
    return print('Please provide valid list')
  
  min = max = list[0]
  for val in list:
    if val > max:
      min, max = max, val
    elif val > min:
      min = val
  return min, max

print(min_max([0, 2, 4, 3, 5]))