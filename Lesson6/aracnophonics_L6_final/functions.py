import random, os, time


# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.
def check_word():
  pass
  
def clear_screen():
  time.sleep(0.3)
  os.system('cls' if os.name == 'nt' else 'clear')

def is_guess_correct(guess, word):
  return guess.lower() in word

def is_guess_valid(guess):
  return guess.isalpha() and len(guess) == 1

# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(correct, word):
  new_word = list('_'*len(word))
  for guess in correct:
    for i, letter in enumerate(word):
      if guess == letter:
        new_word[i] = letter
  print(f'Word = {' '.join(new_word)}')
    

def print_wrong_guesses(incorrect):
  if incorrect:
    new_incorrect = ', '.join(incorrect)
    print(f'Incorrect guesses = {new_incorrect}')

# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries,spiderList):
  spiderList[tries]()
  

#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
  wordList = open('Lesson6/aracnophonics_L6_final/words.txt').read().split()
  word = random.choice(wordList)
  return word

#Put the introduction code/input player name into here 
def introduction():
  name = input("Hello, what's your name? ")
  print(f'Welcome to the game, {name}!')
  print('Loading game...')
  time.sleep(2)