def vowels(input):
  if not bool(input):
    return "Invalid input"
  vowel = 'aeiou'
  count = 0
  for char in input:
    if vowel.__contains__(char):
      count += 1

  print("Total vowels", count)

vowels("abcdefghijhkmnopqrstuvwxyz")
