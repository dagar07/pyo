def catch_error():
  b = []
  try:
   b[1] = 2 
  except IndexError as err:
    print(err)
    print("Don't try buffer overflow attacks in python")

catch_error()