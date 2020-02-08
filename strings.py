def words(letters, word=''):
  letters or print(word)
  for letter in letters:
    words(letters - {letter}, word + letter)

words(set('catdog'))