#access libraries and py files 
import spiderDraw as sd
import functions as md

#Game Loope
def play_game():
  correct = []  #List of correct letters guessed
  incorrect = []  #List of incorrect letters guessed
  spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]
  md.introduction()
  #generate a random word from word list
  word = md.generate_word() 
  trials = 0
  while not md.won_game(correct, word) and not md.lost_game(incorrect): 
    md.clear_screen()
    md.print_spider(len(incorrect),spiderList)
    md.print_word(correct, word)
    md.print_wrong_guesses(incorrect)
    print(f'Trials: {trials}\n')

    guess = input('Guess a letter: ')
    if not md.is_guess_valid(guess):
      print('Guess must be a single letter\n')
    elif md.is_guess_correct(guess, word):
      correct.append(guess.lower())
      print('Correct guess!\n')
    elif guess in correct or guess in incorrect:
      print('Already guessed that')
    else:
      incorrect.append(guess.lower())
      print('Incorrect\n')
    
    trials += 1
    if md.won_game(correct, word) or md.lost_game(incorrect):
      if md.won_game(correct, word):
        md.clear_screen()
        md.print_spider(len(incorrect),spiderList)
        md.print_word(correct, word)
        print('\nYou win!')
      elif md.lost_game(incorrect):
        print('Oh, no! The spider get you.\nGame Over.')
      print(f'The word is: {word.upper()}')
      print(f'It took you {trials} trials\n')
      play_again = input('Do you wanna play again?(y/n) ')
      return play_again.lower() == 'y'
      
playing = True
while playing:
  playing = play_game()
  md.clear_screen()
