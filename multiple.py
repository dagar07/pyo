def is_multiple(n, m):
  if (not bool(n)) | (not bool(m)):
    return False
  
  if n % m == 0:
    return True

  return False
print(is_multiple(9, 4))