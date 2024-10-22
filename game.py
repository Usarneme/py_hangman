import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
unguessed_letters = 'abcdefghijklmnopqrstuvwxyz'

def get_all_words(filename):
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      words = contents.split()
      return words
  except FileNotFoundError:
    print(f"Unable to read file {filename} contents... Please try again.")

def pick_a_random_word(words):
  random_int = random.randint(0, len(words))
  return words[random_int]

filename = 'words.txt'
words = get_all_words(filename)
print("Loaded all words...")
answer_word = pick_a_random_word(words)
print(f"Selected a random word: {answer_word}")
guessed_letters = '_' * len(answer_word)
number_of_guesses = 0;
print(f"Underscored the word: {guessed_letters}")

solved = False
while not solved and number_of_guesses < 10:
  print(f"Remaining letters not yet guessed include '{unguessed_letters}'")
  guess = input('Please guess a letter: ')
  if len(guess) > 1 or guess not in alphabet:
    print('Please only enter a single letter at a time.')
    continue
  if guess not in unguessed_letters:
    print(f"'{guess}' was already guessed. Please try again.")
  else:
    # remove the guess from the unguessed_letters list
    unguessed_letters = unguessed_letters.replace(guess, "", 1)
    # if the guessed letter is in the answer_word, replace the _ with the guessed letter
    if guess in answer_word:
      print(f"Good guess! '{guess}' is in the word.")
      indices = [i for i, char in enumerate(answer_word) if char == guess]
      for index in indices:
        guessed_letters = guessed_letters[:index] + guess + guessed_letters[index + 1:]
    else:
      print(f"Nope! '{guess}' is not in the word.")
    # increment number of guesses
    number_of_guesses += 1
    print(f"After {number_of_guesses} guesses, your word is: {guessed_letters}")

  if '_' not in guessed_letters:
    solved = True

if solved:
  print(f"You win! The word was {answer_word}.")
else:
  print(f"You did not win! The word was {answer_word}.")

print("Exiting the game...")
