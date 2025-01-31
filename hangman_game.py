#import necessary modules
import random, signal, time

#list of words to be used for the hangman game
use = ['goat', 'cow', 'dog', 'giraffe', 'tortoise']
hint = 'animal'

#declaring of global variables
word = ''
guessed = ''
hangman_count = 0
wrong_guesses = []
counter = 0
assist_count = 0
assist_num1 = 0
assist_num2 = 0

def start(lst):
    global hint
    global word
    global guessed

    initialize()

    print('''
Instructions:
1. This game is only available in the English Language.
2. If you need help in guessing a letter type 'help' in the 'Input Guess'.
''')
    #word_list = lst
    level_count = 0
    list_count = len(lst)
    while any(lst):
        level_count +=1
        word = random.choice(lst)

        print(f'Welcome to level {level_count}')

            
        print('\nGuess the word.\n')
        print('- ' * len(word)+'\n[The word has ' + str(len(word)) + ' letters.]')  #put exact number of dashes corresponding to the word
        print(f'Hint: {hint}')
        if len(word) > 5:
            print(f'Only 2 assists [help] available for this word.')
        if len(word) < 5:
            print(f'Only 1 assist [help] available for this word.')
        guess_letter(word)

        if check_same_characters(word, guessed):
            initialize()

        lst.remove(word)
        print(f'Congratulations! Level {level_count}/{list_count} completed.')
        time.sleep(0.3)
    else:
        print('You won!')
            

def guess_letter(arg):
    """

    """

    global word
    global guessed
    global wrong_guesses

    u1 = word
    u2 = str()
    u3 = 0
    u4 = []
    u5 = dict()
    for i in u1:
        u2 =str(u3)+i
        u3+=1
        #print(u2)
        u4.append(u2)
        u5 = dict(u4)
    #print('u5: '+str(u5))

    v1 = ' '*len(word)
    v2 = str()
    v3 = 0
    v4 = []
    for i in v1:
        v2 =str(v3)+i
        v4.append(v2)
        v5 = dict(v4)
        v3+=1
    #print('v5: '+str(v5))

    x1 = str()
    repeated_guess_count1 = 0
    repeated_guess_count2 = 0
    while x1 != u1:
        guess = input('\nInput guess: ')

        #For master control: shows the word to be guessed.
        if guess.lower() == 'master':
            print(cheat(word))
        
        elif guess.lower() == 'help':
            w1 = u5
            w2 = v5
            w3 = 0
            assist = need_help(word)
            for k,v in dict(u5).items():
                for a,b in dict(v5).items():
                    if assist == v:
                        w3 += 1
                        if w3 == 1:
                            w2[k] = v
                            guessed = guessed+w1[k]
                            del w1[k]

            x1 = str()
            for k,v in dict(w2).items():
                x1 = x1+v
            print('\n' + ' '.join(x1) + '\n' + '- ' * len(word))
            continue
        elif guess.isalpha() and len(guess) == 1:
            e = guess.lower()
                
            w1 = u5
            w2 = v5
            w3 = 0

            
            if repeated_guess_count1 > 1 or repeated_guess_count2 > 1:
                hangman()
            
            if e in arg:
                if e in guessed:
                    if arg.count(e) > 1 and arg.count(e) == guessed.count(e):
                        print(f'Your guess \'{e}\' has exceeded the number of times it was repeated in the word. Guess again.')
                        repeated_guess_count1 += 1
                    
                    if arg.count(e) == 1:
                        print(f'You\'ve guessed letter \'{e}\' already. Guess again.')
                        repeated_guess_count2 += 1

                for k,v in dict(u5).items():
                    for a,b in dict(v5).items():
                        if e == v:
                            w3 += 1
                            if w3 == 1:
                                w2[k] = v
                                print('Correct guess!')
                                #print('w1: '+str(w1))
                                #print('w2: '+str(w2))
                                guessed = guessed+w1[k]
                                #print('guessed: '+guessed)
                                del w1[k]
                #print('w1: '+str(w1))
                #print('w2: '+str(w2))

                x1 = str()
                for k,v in dict(w2).items():
                    x1 = x1+v
                print('\n' + ' '.join(x1) + '\n' + '- ' * len(word))
                    
            else:
                hangman()
                wrong_guesses.append(e)
                wrong_guesses.sort()
                print('List of wrong guesses: ' + ', '.join(wrong_guesses))

        elif guess.isalpha() and len(guess) > 1:
            print('Kindly input one letter at a time or \'help\' for assistance.')

        else:
            print('Kindly input a valid English letter.')


def initialize():
    """
    Cleares stored values in case of an exit, failure or game completion.
    """
    global word
    global guessed
    global wrong_guesses
    global hangman_count
    global assist_num1
    global assist_num2
    global assist_count

    #word = ''
    guessed =''
    wrong_guesses = []
    hangman_count = 0
    assist_num1, assist_num2, assist_count = 0,0,0

def cheat(arg):
    return arg

def need_help(arg):
    global assist_count
    global assist_num1
    global assist_num2
    
    if len(arg) > 5:
        if assist_count < 2:
            assist = random.choice(arg)
            #print(f'1 assist used, {assist_num1} left')
            assist_num1 += 1
            print(f'{assist_num1}/2 assist used.')
        else:
            print(f'Sorry, no assist left')
            assist = ''
        
    elif len(arg) < 5:
        if assist_count < 1:
            assist = random.choice(arg)
            #print(f'1 assist used, {assist_num2} left')
            assist_num2 += 1
            print(f'{assist_num2}/1 assist used.')
        else:
            print(f'Sorry, no assist left')
            assist = ''
    assist_count += 1
    
    return assist
    
    

def check_same_characters(str1, str2):
    """
    Checks if two strings have the same characters, regardless of order.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if the strings have thesame characters, False otherwise.
    """

    # Create dictionaries to count character frequencies
    char_count1 = {}
    char_count2 = {}

    # Count character frequencies in str1
    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
                
    # Count character frequencies in str2
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Compare character frequencies
    return char_count1 == char_count2
    
        
def hangman():
    """

    """
    global hangman_count
    
    #hangman images in case of a wrong guess
    hang = ['''
        +---+
        |   |
            |
            |
            |
            |
    ------------- ''', '''
        +---+
        |   |
        0   |
            |
            |
            |
    ------------- ''', '''
        +---+
        |   |
        0   |
        |   |
            |
            |
    ------------- ''', '''
        +---+
        |   |
        0   |
       /|   |
            |
            |
    ------------- ''', '''
        +---+
        |   |
        0   |
       /|\  |
            |
            |
    ------------- ''', '''
        +---+
        |   |
        0   |
       /|\  |
       /    |
            |
    ------------- ''', '''
        +---+
        |   |
        0   |
       /|\  |
       / \  |
            |
    ------------- ''']

    game_over = ['    +---+', '    |   |', '    0   |', '   /|\  |', '   / \  |', '        |', '------------- ']

    
    if any(list(hang)):
        print('Wrong guess!')
        print(hang[hangman_count])
        hang.remove(hang[hangman_count])
        if hangman_count == len(hang):
            time.sleep(1.5) #Add a 1.5 second pause here
            print('\nGame over!\n')
            for i in game_over:
                print(i)
                time.sleep(0.1) #Add a 1.5 second pause here
            lose()
    hangman_count += 1
    
    
    


def end():
    print('Thanks for playing my game.')
    time.sleep(1)
    exit()

def lose():
    print('Unfortunately, you lost. \nThanks for playing my game.')
    time.sleep(1)
    exit()

def signal_handler(sig, frame): #function for signal handling like ctrl+c interruption
    
    print('Abrupt code interruption with Ctrl+C detected.')
    program_end = input('Do you wish to end the program? Y or N ')
    false_count = 0
    while True:
        
        if program_end.isalpha() and len(program_end) == 1:
            a = program_end.lower()
            if a == 'y':
                print('Goodbye!')
                time.sleep(1.5) #Add a 1.5 second pause here
                initialize()
                end()
            elif a == 'n':
                print('Let\'s continue please.')
            break
        else:
            program_end = input('Y for yes and N for no. So Y or N? ')
            if program_end.isalpha() and len(program_end) == 1:
                a = program_end.lower()
                if a == 'y':
                    initialize()
                    end()
                elif a == 'n':
                    print('Let\'s continue please.')
            else:
                false_count += 1
                if false_count > 2:
                    print('I\'m sorry but I have to end your session now.\nTo play again, kindly restart the game.')
                    end()
                


signal.signal(signal.SIGINT, signal_handler)    #for signal handling

start(use)

#Try/Except
#function best practices
#ask Rapture for data
#submit
#school work: diary, lesson plan, lesson notes
#next alphacode task
