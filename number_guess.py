number = 40
question = "What is the 2 digits number: "

while True:
  guess = int(input(question))
  if guess > number:
    print("Little lower")
  elif guess < number:
    print("Little higher")
  else:
    print("Right guess: ",guess)
    break
