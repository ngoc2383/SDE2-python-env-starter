# Restate: write a function to determine how many vowels (a e i o u) is in the input
# Input: string of text
# Output: number (int) of vowels in the string
# Important piece of datas: text (input), vowels_num (output)
# Clarifying: what if the user enter a non-string input

# DEF vowels_count(text):
    # FOR loop through each char of the text
        # IF the char is a vowel
            # ADD 1 to vowels_num
    # RETURN vowels_num
# PRINT vowels_num


def vowels_count(text):
    vowels_num = 0
    for char in text.lower():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowels_num += 1
    
    return vowels_num

print(vowels_count("hEllo World"))