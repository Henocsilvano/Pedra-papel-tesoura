from time import sleep
from random import choice

def player():
    print('~'*52)
    print('\033[32m» You are going to play with the computer, make your\nchoice based in this numbers below:\033[m')
    print('~'*52)
    options = ['Rock', 'Paper', 'Scissors']
    for k, value in enumerate(options):
        print(f'[\033[34m{str(k+1)}\033[m] = \033[36m{value}\033[m')
    computer = choice(options)
    def msg():
        print(f'')
    while True:
        while True:
            try:
                print('~'*52)
                player = int(input('\033[36mPlay: \033[m'))
            except ValueError:
                print('~'*52)
                print('Type a whole number ')
                continue
            else:
                break
        if  player < 1  or player > 3:
            print('~'*52)
            print('Invalid option!')
            continue
        else:
            break
    if options[player-1] == computer:
        return f'\033[32mThe computer chose {computer} and, you chose {options[player-1]}\n\nIt is Tie!!\033[m'
    
    if you_win(player, computer, options):
        return f'\033[32mThe computer chose {computer} and, you chose {options[player-1]}\n\nYou won!\033[m'
    
    return f'\033[32mThe computer chose {computer} and, you chose {options[player-1]}\n\nYou lost!\033[m'

def you_win(player, computer, options):
    if (options[player-1] == 'Rock' and computer == 'Scissors') or (options[player-1] == 'Paper' and computer == 'Rock')\
         or (options[player-1] == 'Scissors' and computer == 'Paper'):
        return True
    return False

print('~'*52)
print(f"\033[32m{'Well come to ROCK, PAPER, SCISSORS game!':^52}\033[m")
print('~'*52)
while True:
    play = player()
    print('~'*52)
    print(play)
    print('~'*52)
    ans = ' '
    while ans not in 'YN':
        try:
            ans = input('\033[36mPlay again? [Y/N]:\033[m').strip().upper()[0]
        except:
            print('Type N for No or type Y for Yes.')
            continue

    if ans == 'N':
        print('~'*52)
        print('\033[32mNice game, come back always!\033[m\n')
        break