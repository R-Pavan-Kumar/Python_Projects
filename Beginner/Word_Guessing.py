import random

def find_word(guess, random_word, length, word_guess, hints):
    if length == 0:
        print('You took {} extra chances with {} hints to guess the word.'.format(guess+hints-len(random_word), hints))
        choice()
    else:
        print('Enter a letter :')
        letter = input()
        if letter == 'hint':
            Hint(guess, random_word, length, word_guess, hints)
        elif letter in random_word:
            guess += 1
            length -= 1
            word_guess[random_word.index(letter)] = letter
            random_word[random_word.index(letter)] = '_'
            print(*word_guess)
            find_word(guess, random_word, length, word_guess, hints)
        else:
            print("oops! try again")
            guess += 1
            find_word(guess, random_word, length, word_guess, hints)
            
    pass

def selection():
    random_word = random.choice(main_list)
    length = len(random_word)
    word_guess = ' '
    if random_word in fruit_list:
        print('The word is the name of a fruit with {} letters.'.format(length))
    elif random_word in animal_list:
        print('The word is the name of an animal having {} letters.'.format(length))
    else:
        print('The word is the name of a bird {} with letters.'.format(length))
    
    for _ in range(length):
        word_guess += '_ '
    word_guess = list(word_guess.split())
    random_word = list(random_word)
    print(*word_guess)

    guess,hints = 0,0
    find_word(guess, random_word, length, word_guess, hints)
    pass

def Hint(guess, random_word, length, word_guess, hints):
    random_number = random.randint(0,length)
    if hints > length//2:
        print('Maximum number of hints reached.')
        print(*word_guess)
        find_word(guess, random_word, length, word_guess, hints)
    elif random_word[random_number] == '_' and random_number < length:
        Hint(guess, random_word, length, word_guess, hints)
    else:
        if random_number < length:
            word_guess[random_number] = random_word[random_number]
            random_word[random_number] = '_'
            length -= 1
            #guess += 1
            hints += 1
            print(*word_guess)
            find_word(guess, random_word, length, word_guess, hints)
    pass

def choice():
    print('Do you want to play again ? \n Enter y for YES and n for NO')
    ch = input()
    if ch == 'y':
        selection()
    else:
        exit()
    pass


print("Welcome to word guessing game! \nEnter your name :")
name = input()

print("All the best {}.".format(name))

main_list = ['Mango', 'Apple', 'Orange', 'Grape', 'Guava', 'Watermelon', 'Strawberry', 'Pineapple', 'Banana', 'Kiwi', 'Cat', 'Dog', 'Camel', 'Lion', 'Tiger', 'Elephant', 'Horse', 'Rabbit', 'Monkey', 'Deer', 'Parrot', 'Eagle', 'Sparrow', 'Pigeon', 'Peacock', 'Vulture', 'Swan', 'Crow', 'Owl']

fruit_list = ['Mango', 'Apple', 'Orange', 'Grape', 'Guava', 'Watermelon', 'Strawberry', 'Pineapple', 'Banana', 'Kiwi']

animal_list = ['Cat', 'Dog', 'Camel', 'Lion', 'Tiger', 'Elephant', 'Horse', 'Rabbit', 'Monkey', 'Deer']

bird_list = ['Parrot', 'Eagle', 'Sparrow', 'Pigeon', 'Peacock', 'Vulture', 'Swan', 'Crow', 'Owl']


print('click s to start the game \n or \nclick e to exit the game')
c = input()

if c == 's':
    print('If you want any hint, enter "hint" at any stage during the game')
    selection()