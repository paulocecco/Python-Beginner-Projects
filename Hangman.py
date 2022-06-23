from words import word
import random

def hangman():
    life = 0
    win = 0
    hangword = random.choice(word).upper()
    dashes = '_'*len(hangword)
    word_usen = list()
    while life < 6:
        us_let = str(input('Find the word. Enter a letter: ')).upper()
        #Right letter
        if us_let in hangword:
            letpos = [pos for pos, char in enumerate(hangword) if char == us_let]
            print(len(letpos))
            for i in letpos:
                dashes = dashes[:i] + us_let + dashes[i+1:]
                win += 1
            print('\n',dashes)
            #Victory
            if win == len(hangword):
                print('You won')
                restart()
                break
            else: 
                pass

        #Letter repeated
        elif us_let in word_usen:
            life = life
            win = win
            print(f'The word {us_let} has already been used. Please select another one.')
            print('Letters used: ', word_usen)
            print('\n',dashes)
            continue

        #Wrong letter
        else:
            word_usen.append(str(us_let))
            print('Letters used: ', word_usen)
            life += 1
            print(f"Letter {us_let} not in the word.")
            if life == 1:
                print('There goes the head')
                print(word_usen)
                print('\n',dashes)
            elif life == 2:
                print('There goes the body')
                print(word_usen)
                print('\n',dashes)
            elif life == 3:
                print('There goes the right arm')
                print(word_usen)
                print('\n',dashes)
            elif life == 4:
                print('There goes the left arm')
                print(word_usen)
                print('\n',dashes)
            elif life == 5:
                print('There goes the right leg')
                print(word_usen)
                print('\n',dashes)
            elif life == 6:
                print('There goes the left leg')
                print(word_usen)
                print('\n',dashes)
            else:
                continue

    else:
        print(f'You were hanged by {hangword}. If you didn\'t appreciate your life, I hope you don\'t do the same in the after one.')
        restart()

def restart():
    choice = input('Want to replay?:' ).upper()
    if choice in 'YES':
        hangman()
    elif choice in 'NO':
        print('See ya!')
        exit
    else:
        print('Wrong input try again')
        restart()

hangman()

