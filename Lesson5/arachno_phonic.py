'''
Import a random library
Initialize a word_bank to randomly selected from

Initialize dashes as empty list
    For loop through each char in target_word
        Append a dash to dashes list
    Join dashes list and display to the user
Define game function
    Initialize target_word using random.choice(word_bank)

    While loop dashes != target_word
        Prompt user to input their guess
        If guess is in target_word, update the dashes with the correct guess
        Else print error message, update spider
    Print You win!

'''