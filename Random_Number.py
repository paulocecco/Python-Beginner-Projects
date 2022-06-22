import random

def guessnumber_easy():
    life = 0
    computernumber = random.randint(0,10)
    while life < 5:
        usernumber = int(input("Guess the number!: "))
        if usernumber != computernumber:
            print('Wrong guess!')
            life = life+1
        else:
            print("Number found!")
            break
    restart()

def guessnumber_medium():
    life = 0
    computernumber = random.randint(0,15)
    while life < 4:
        usernumber = int(input("Guess the number!: "))
        if usernumber != computernumber:
            print('Wrong guess!')
            life = life+1
        else:
            print("Number found!")
            break
    restart()

def guessnumber_hard():
    life = 0
    computernumber = random.randint(0,20)
    while life < 3:
        usernumber = int(input("Guess the number!: "))
        if usernumber != computernumber:
            print('Wrong guess!')
            life = life+1
        else:
            print("Number found!")
            break
    restart()

def guessnumber_impossible():
    life = 0
    computernumber = random.randint(0,50)
    while life < 1:
        usernumber = int(input("Guess the number!: "))
        if usernumber != computernumber:
            print('Wrong guess!')
            life = life+1
        else:
            print("Number found!")
            break
    restart()

def quitting():
    quit = input("Want to Quit. Yes or No?: ").capitalize()
    if quit == "Yes":
        exit
    elif quit == "No":
        dificulty()
    else:
        print("Not a valid option, quitting")
        exit

def restart():
    rest = input("Want to restart. Yes or No?: ").capitalize()
    if rest == "Yes":
        dificulty()
    elif rest == "No":
        exit
    else:
        print("Not a valid option, quitting")
        exit

def dificulty():
    dific = int(input("Enter dificulty: "))
    if dific == 1:
        guessnumber_easy()
    elif dific == 2:
        guessnumber_medium()
    elif dific == 3:
        guessnumber_hard()
    elif dific == 4:
        guessnumber_impossible()
    else:
        print("Not a valid option")
        quitting()

dificulty()