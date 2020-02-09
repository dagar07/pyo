# this function reverse a string like
# I Love You => You Love I
def reverse_string (str):
  if not bool(str):
    return 'Invalid String'
  
  word = ''
  reversStr = ''
  for letter in str:
    word = word + letter
    if letter == ' ':
      reversStr = word + reversStr
      word= ''
  reversStr = word + ' ' + reversStr
  return reversStr

print(reverse_string('i like this program very much'))