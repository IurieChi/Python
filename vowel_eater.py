# vowel eater

def vowel_eater():
    # Prompt the user to enter a word
    user_word = input('Enter a word: ')
    user_word =user_word.upper() #convert all words to upper case leters

    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            print(letter)

def vowel_eater_2():
    # Prompt the user to enter a word
    user_word = input('Enter a word: ')
     #convert all words to upper case leters
    word_without_vowels= ''

    for letter in user_word.upper():
        if letter in "AEIOU":
            continue
        else:
            word_without_vowels +=letter    
    print(word_without_vowels)

# vowel_eater()
vowel_eater_2()