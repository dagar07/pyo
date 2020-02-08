def get_index(str, negative_index):
  if not bool(str):
    return 'Please provide valid string'
  
  index = len(str) + negative_index
  return print('Str -ve index, +ve index', str, negative_index, str[negative_index], index, str[index])

get_index('karan', -3)