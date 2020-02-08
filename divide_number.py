def divide_number(number, count = 0):
  if number // 2 >= 2:
    count += 1
    return divide_number(number // 2, count)
  return count + 1

def get_number():
  a = int(input("Enter number grater than 2: "))
  if a < 2:
    return print("Invalid number")
  count = divide_number(a)
  print(count)

get_number()
