import random
#print('Machine:', machine, '| User:', user)
def RPS():
    #System points
    Upoints = 0 
    Mpoints = 0
    while ((Mpoints or Upoints) < 3):
        #System choice
        kachipum = ['Rock', 'Paper', 'Scissors']
        machine = random.choice(kachipum)
        user = input('Select one between Rock (R), Paper (P), Scissors (S): ').capitalize()
        if user in 'Scissors':
            user = 'Scissors'
        elif user in 'Rock':
            user = 'Rock'
        elif user in 'Paper':
            user = 'Paper'
        else:
            print('Wrong input, try again.')
            user = input('Select one between Rock (R), Paper (P), Scissors (S): ').capitalize()
        print('Rock, Paper, Scissors!')
        #System Game
        if user == 'Rock' and machine == 'Scissors':
            Upoints = Upoints + 1
            print('Machine chose:', machine, '| User chose:', user, '\n Rock beats Scissors')
            print('Machine points:', Mpoints, '| User points:', Upoints)
        elif user == 'Rock' and machine == 'Paper':
            Mpoints = Mpoints + 1
            print('Machine chose:', machine, '| User chose:', user, '\n Paper wraps Rock')
            print('Machine points:', Mpoints, '| User points:', Upoints)
        elif user == 'Scissors' and machine == 'Paper':
            Upoints = Upoints + 1
            print('Machine chose:', machine, '| User chose:', user, '\n Scissors cut Paper')
            print('Machine points:', Mpoints, '| User points:', Upoints)
        elif user == 'Scissors' and machine == 'Rock':
            Mpoints = Mpoints + 1
            print('Machine chose:', machine, '| User chose:', user, '\n Rock beats Scissors')
            print('Machine points:', Mpoints, '| User points:', Upoints)
        elif user == 'Paper' and machine == 'Rock':
            Upoints = Upoints + 1
            print('Machine chose:', machine, '| User chose:', user, '\n Paper wraps Rock')
            print('Machine points:', Mpoints, '| User points:', Upoints)
        elif user == 'Paper' and machine == 'Scissors':
            Mpoints = Mpoints + 1
            print('Machine chose:', machine, '| User chose:', user, '\n Scissors cut Paper')
            print('Machine points:', Mpoints, '| User points:', Upoints)
        else:
            Upoints = Upoints + 0
            Mpoints = Mpoints + 0
            print('Machine chose:', machine, '| User chose:', user, '\n Tie')
            print('Machine points:', Mpoints, '| User points:', Upoints)
             
    #Winning
    if Mpoints > Upoints:
        print('Machine wins:', Mpoints, 'against', Upoints)
        rematch()
    elif Upoints > Mpoints:
        print('User wins:', Upoints, 'against', Mpoints)
        rematch()
    else:
        print('Point error')
        exit

def rematch():
    #Rematch
    rema = input('Want a rematch? Yes (Y) or No (N): ').capitalize()
    if rema in 'Yes':
        RPS()
    elif rema in 'No':
        print('Quiting game.')
        exit
    else:
        print('Wrong input, try again.')
        rematch() 

RPS()