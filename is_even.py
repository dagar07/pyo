def is_even(k):
  isVal = k & 1
  
  if isVal == 0:
    return print('Number is even:', k)
  return print('Number is odd:', k)

is_even(100001)