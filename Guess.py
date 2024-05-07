import random

# Define difficulty level (change range for harder/easier game)
min_number = 1
max_number = 100

# Welcome message
print("Welcome to the Number Guessing Game!")

# Generate random number
secret_number = random.randint(min_number, max_number)
guesses_left = 10  # Set number of guesses allowed

while guesses_left > 0:
  # Get user guess
  try:
    guess = int(input(f"Guess a number between {min_number} and {max_number} (You have {guesses_left} guesses left): "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue  # Skip to next iteration if input is not a number

  # Check guess
  guesses_left -= 1
  if guess == secret_number:
    print(f"Congratulations! You guessed the number in {10 - guesses_left} tries.")
    break  # Exit loop if guess is correct
  elif guess < secret_number:
    print("Your guess is too low. Try again!")
  else:
    print("Your guess is too high. Try again!")

# Game over message
if guesses_left == 0:
  print(f"Sorry, you ran out of guesses. The number was {secret_number}.")
