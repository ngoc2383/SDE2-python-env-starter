import functions as f
word = f.generate_word()
def play_game():
    tries = 0
    guess_list = []
    color_codes = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guessed_letters = []
    guess = ''
    f.introduction()

    while tries < 6 and f.won_game(guess, word) == False:
        f.print_directions()
        alphabet, guessed_letters = f.print_guesses(guess_list, color_codes, alphabet, guessed_letters)
        f.print_alphabet(alphabet)
        guess = input('\nEnter your guess: ').lower().strip()
        
        if len(guess) < 5 or len(guess) > 5:
            print('Must be a 5-letter word')
        elif ' ' in word:
            print('Must not have any space in between letters')
        elif not guess.isalpha():
            print('No digits or special characters allowed')
        else:
            guess_list.append(guess)
            color_codes.append(f.check_word(guess, word))
            tries += 1
        
        f.clear_screen()
        if f.won_game(guess, word):
            f.clear_screen()
            f.print_guesses(guess_list, color_codes, alphabet, guessed_letters)
            print(f'The word is: {word.upper()}')
            print(f'It took you {tries} trials\n')
            play_again = input('Do you wanna play again?(y/n) ')
            return play_again.lower() == 'y'
    print('You lose.')
    play_again = input('Do you wanna play again?(y/n) ')
    return play_again.lower() == 'y'
        

playing = True
while playing:
    playing = play_game()
    f.clear_screen()
print('Thank you for playing!')
    