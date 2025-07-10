import time, os, random

def clear_screen():
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

def introduction():
    name = input('Hello, what is your name? ')
    print(f'Welcome to the game, {name}.\nLoading game...')
    clear_screen()

def print_directions():
    print('DIRECTIONS:')
    print("1. Guess the 5-letter word in 6 tries.")
    print("2. After each guess, letters will be colored:")
    print("   - Green: correct letter & position")
    print("   - Yellow: letter in word but wrong position")
    print("   - Gray: letter not in word")
    print("3. Enter 5-letter words with letters a-z.")
    print('---------------------------------------------\n')

word_bank = [
    "plant", "brisk", "glide", "stone", "flame",
    "crane", "spine", "quirk", "drift", "blush",
    "grape", "slope", "charm", "frost", "track",
    "pride", "swing", "flock", "brush", "climb"
]

def generate_word():
    word = random.choice(word_bank)
    word_bank.remove(word)
    return word

green = '\033[32m'
yellow = '\033[33m'
gray = '\033[90m'
def check_word(guess, word):
    char = list(guess)
    color_code = []
    for i in range(len(char)):
        if char[i] in word:
            if char[i] == word[i]:
                color_code.append(green)
            else:
                color_code.append(yellow)
        else:
            color_code.append(gray)
    return color_code

def print_guesses(guesses, colors, alphabet, guessed_letters):
    for i, guess in enumerate(guesses):
        color_set = colors[i]
        print(f'Trial {i+1}: ', end='')
        for k, letter in enumerate(guess):
            print(color_set[k] + letter + '\033[0m', end=' ')
            
            if letter not in guessed_letters:
                guessed_letters.append(letter)
                index = alphabet.index(letter)
                alphabet[index] = color_set[k] + letter + '\033[0m'
            
        print('\n')
    return alphabet, guessed_letters

def won_game(guess, word):
    return guess == word

def print_alphabet(alphabet):
    for char in alphabet:
        print(char, end=' ')
    print()