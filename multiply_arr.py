def arr_multiply(a, b):
  if not bool(a) or not bool(b):
    return "Invalid Inputs"
  
  c = []
  for index in range(len(a)):
    c.append(a[index] * b[index])

  return c

print(arr_multiply([1, 2, 3], [4, 5, 6]))
