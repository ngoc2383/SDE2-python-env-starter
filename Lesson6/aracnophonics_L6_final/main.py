#access libraries and py files 
import spiderDraw as sd
import functions as md

#Initialize variables and setup 
#Need to keep track of correct letters, incorrect letters and tries

correct = []  #List of correct letters guessed
incorrect = []  #List of incorrect letters guessed
tries = 0   #Number of incorrect guesses
game = True 

#Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]


#Print intro statements (welcome to game, etc)
md.introduction()


#generate a random word from word list
word = md.generate_word()  



#Game Loop
while game: 
  md.clear_screen()
  md.print_spider(tries,spiderList)
  md.print_word(correct, word)
  md.print_wrong_guesses(incorrect)
  print()
  guess = input('Guess a letter: ')
  if md.is_guess_correct(guess, word):
    correct.append(guess)
    print('Correct guess!\n')
  elif not md.is_guess_valid(guess):
    print('Guess must be a single letter\n')
  elif guess in correct or guess in incorrect:
    print('Already guessed that')
  else:
    incorrect.append(guess)
    print('Incorrect\n')
    tries += 1
    
  #This is where you'll call all of your functions. Just need to decide the proper order.


  #You will also need to specify your win and lose conditions in here